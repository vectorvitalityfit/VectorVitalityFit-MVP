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
        #set subscription
        run_cmd(f"az account set --subscription {subscription_id}") 
