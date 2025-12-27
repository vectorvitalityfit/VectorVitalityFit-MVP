from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import ManagedOnlineEndpoint, ManagedOnlineDeployment, Model, Environment, CodeConfiguration

subscription_id = "7cd27f16-62c4-43e9-8709-f1ea88ede961"
resource_group = "VVF-Resources"
workspace_name = "VVF-Workspace"

def deploy_model():
    credential = DefaultAzureCredential()
    ml_client = MLClient(credential, subscription_id, resource_group, workspace_name)

    # Register your model
    model = Model(path="score.py", name="muscle-growth-model", description="Muscle growth prediction model")
    ml_client.models.create_or_update(model)

    # Create or update environment from conda_env.yml
    env = Environment(
        name="muscle-growth-env",
        conda_file="conda_env.yml",
        image="mcr.microsoft.com/azureml/base:latest"
    )
    env = ml_client.environments.create_or_update(env)

    # Create or update endpoint
    endpoint = ManagedOnlineEndpoint(name="musclegrowth-endpoint", auth_mode="key", description="Muscle growth model API endpoint")
    ml_client.online_endpoints.begin_create_or_update(endpoint).result()

    # Define code configuration (path to your code and scoring script)
    code_config = CodeConfiguration(code="./", scoring_script="score.py")

    # Deploy model with environment and code configuration
    deployment = ManagedOnlineDeployment(
        name="production",
        endpoint_name=endpoint.name,
        model=model.id,
        environment_id=env.id,
        code_configuration=code_config,
        instance_type="Standard_DS3_v2",
        instance_count=1
    )
    ml_client.online_deployments.begin_create_or_update(deployment).result()

    # Route all traffic to this deployment
    endpoint.traffic = {"production": 100}
    ml_client.online_endpoints.begin_create_or_update(endpoint).result()

    print("Model deployed to endpoint:", endpoint.name)
    print("Scoring URI:", endpoint.scoring_uri)

if __name__ == "__main__":
    deploy_model()