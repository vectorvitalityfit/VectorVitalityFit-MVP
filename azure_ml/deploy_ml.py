from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import ManagedOnlineEndpoint, ManagedOnlineDeployment, Model

subscription_id = "7cd27f16-62c4-43e9-8709-f1ea88ede961"
resource_group="VVF-Resources"
workspace_name="VVF-Workspace"

def deploy_model():
    credential=DefaultAzureCredential()
    ml_client=MLClient(credential, subscription_id, resource_group, workspace_name)

    model=Model(path="model.py", name="muscle-growth-model", description="Muscle growth prediction model")
    ml_client.models.create_or_update(model)

    endpoint=ManagedOnlineEndpoint(name="musclegrowth-endpoint")
    ml_client.online_endpoints.begin_create_or_update(endpoint).result()

    deployment=ManagedOnlineDeployment(
        name="production",
        endpoint_name=endpoint.name,
        model=model.id,
        instance_type="Standard_DS3_v2",
        instance_count=1
    )
    ml_client.online_deployments.begin_create_or_update(deployment).result()
    endpoint.traffic={"production":100}
    ml_client.online_endpoints.begin_create_or_update(endpoint).result()
    print("Model deployed to endpoint:", endpoint.name)

if __name__=="__main__":
    deploy_model()