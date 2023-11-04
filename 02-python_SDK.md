**Connect to the workspace:**
To authenticate, you need the values to three necessary parameters:

- *subscription_id*: Your subscription ID.
- *resource_group*: The name of your resource group.
- *workspace_name*: The name of your workspace.

from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace
)
s
You'll call MLClient anytime you want to create or update an asset or resource in the workspace.

from azure.ai.ml import command

# configure job
job = command(
    code="./src",
    command="python train.py",
    environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest",
    compute="aml-cluster",
    experiment_name="train-model"
)

# connect to workspace and submit job
returned_job = ml_client.create_or_update(job)