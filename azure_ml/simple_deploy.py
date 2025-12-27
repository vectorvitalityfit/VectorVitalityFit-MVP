import os
import subprocess
import time

subscription_id = "7cd27f16-62c4-43e9-8709-f1ea88ede961"
resource_group = "VVF-Resources"
workspace = "VVF-Workspace"
location = "eastus"
endpoint_name = f"musclegrowth-endpoint-{int(time.time())}"

subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID", "7cd27f16-62c4-43e9-8709-f1ea88ede961")
resource_group = os.getenv("AZURE_RESOURCE_GROUP", "VVF-Resources")
workspace = os.getenv("AZURE_ML_WORKSPACE", "VVF-Workspace")
location = os.getenv("AZURE_LOCATION", "eastus")

# Generate a unique endpoint name with timestamp
endpoint_name = f"musclegrowth-endpoint-{int(time.time())}"

def run_cmd(cmd):
    print(f"Running command: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        raise Exception(f"Command failed: {cmd}")
    else:
        print(result.stdout.strip())
    return result.stdout.strip()

def main():
    try:
        # Set the active subscription
        run_cmd(f"az account set --subscription {subscription_id}")

        # Create resource group (idempotent)
        run_cmd(f"az group create --name {resource_group} --location {location}")

        # Create Azure ML workspace (idempotent)
        run_cmd(f"az ml workspace create --name {workspace} --resource-group {resource_group} --location {location}")

        # Delete existing endpoint if it exists (ignore errors)
        try:
            run_cmd(f"az ml online-endpoint delete --name {endpoint_name} --resource-group {resource_group} --workspace-name {workspace} --yes")
            print("Waiting 10 seconds for deletion to propagate...")
            time.sleep(10)
        except Exception as e:
            print(f"Warning: {e}")

        # Create a new online endpoint
        run_cmd(f"az ml online-endpoint create --name {endpoint_name} --resource-group {resource_group} --workspace-name {workspace} --auth-mode key")

        print(f"Endpoint '{endpoint_name}' created successfully.")

    except Exception as e:
        print(f"Deployment failed: {e}")

if __name__ == "__main__":
    main()
