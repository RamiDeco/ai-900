import os
import json
from dotenv import load_dotenv
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

# Load environment variables
load_dotenv()

# Get environment variables
subscription_id = os.getenv("SUBSCRIPTION_ID")
resource_group = os.getenv("RESOURCE_GROUP")
target_endpoint = os.getenv("TARGET_ENDPOINT")
ws_name = os.getenv("WORKSPACE_NAME")

request_file = "sample_request.json"   

try:
    # Get credentials
    credential = DefaultAzureCredential()

    # Instantiate client
    ml_client = MLClient(credential, subscription_id, resource_group, workspace_name=ws_name)
            
    try:
        # Invoke endpoint
        response = ml_client.online_endpoints.invoke(
            endpoint_name=target_endpoint,
            request_file=request_file,
        )
        print(f"Response:\n{response}")
    except Exception as e:
        print(f"Error invoking endpoint: {e}")
except Exception as e:
    print(f"Error: {e}")