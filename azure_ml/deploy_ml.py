import time
from azure.identity import ClientSecretCredential
from azure.ai.ml import MLClient
from azure.ai.ml.entities import ManagedOnlineEndpoint
from azure.core.exceptions import HttpResponseError

def deploy_model():
    resource_group = "VVF-Resources"
    workspace = "VVF-Workspace"

    ml_client = MLClient(
        credential=credential,
        subscription_id=subscription_id,
        resource_group_name=resource_group,
        workspace_name=workspace
    )

    unique_suffix = str(int(time.time()))
    endpoint_name = f"musclegrowth-endpoint-{unique_suffix}"

    try:
        ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
        print(f"Deleted existing endpoint {endpoint_name}.")
        time.sleep(10)
    except Exception as e:
        print(f"No existing endpoint to delete or delete failed: {e}")

    endpoint = ManagedOnlineEndpoint(
        name=endpoint_name,
        auth_mode="key"
    )

    try:
        ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        print(f"Endpoint {endpoint_name} created successfully.")
    except HttpResponseError as e:
        print("HttpResponseError:", e.message)
        print("Error response:", e.response.text())
        raise
    except Exception as e:
        print("Unexpected error:", e)
        raise

if __name__ == "__main__":
    deploy_model()