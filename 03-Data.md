To find and access data in Azure Machine Learning, you'll use ***Uniform Resource Identifiers (URIs)***.

There are three common protocols when working with data in the context of Azure Machine Learning:

- http(s): Use for data stores publicly or privately in an Azure Blob Storage or publicly available http(s) location.(need authentication info when private)
- abfs(s): Use for data stores in an Azure Data Lake Storage Gen 2.
- azureml: Use for data stored in a datastore.

*Note*: A datastore is a reference to an existing storage account on Azure. When you refer to the datastore however, you won't need to authenticate as the connection information stored with the datastore will be used by Azure Machine Learning.
*Note*:It's considered a best practice to avoid any sensitive data in your code, like authentication information. Therefore, whenever possible, you should work with __datastores__ and data assets in Azure Machine Learning. 

# Create Datastore
When you create a datastore with an existing storage account on Azure, you have the choice between two different authentication methods:

- **Credential-based**: Use a service principal, __shared access signature (SAS) token__ or __account key__ to authenticate access to your storage account.
- **Identity-based**: Use your Microsoft Entra identity or managed identity.

*Create Datastore with Account Key:*

blob_datastore = AzureBlobDatastore(
    			name = "blob_example",
    			description = "Datastore pointing to a blob container",
    			account_name = "mytestblobstore",
    			container_name = "data-container",
    			credentials = AccountKeyCredentials(
        			account_key="XXXxxxXXXxXXXXxxXXX"
    			),
)
ml_client.create_or_update(blob_datastore)

*Create Datastore with SAS Key:*

blob_datastore = AzureBlobDatastore(
name="blob_sas_example",
description="Datastore pointing to a blob container",
account_name="mytestblobstore",
container_name="data-container",
credentials=SasTokenCredentials(
sas_token="?xx=XXXX-XX-XX&xx=xxxx&xxx=xxx&xx=xxxxxxxxxxx&xx=XXXX-XX-XXXXX:XX:XXX&xx=XXXX-XX-XXXXX:XX:XXX&xxx=xxxxx&xxx=XXxXXXxxxxxXXXXXXXxXxxxXXXXXxxXXXXXxXXXXxXXXxXXxXX"
),
)
ml_client.create_or_update(blob_datastore)

# Create Data asset

A Data Asset in Azure ML is a specific piece of data stored in a Datastore. Creating a Data Asset is useful when you want to organize and version specific datasets and track their metadata.

he supported paths you can use when creating a URI file data asset are:

- Local: ./<path>
- Azure Blob Storage: wasbs://<account_name>.blob.core.windows.net/<container_name>/<folder>/<file>
- Azure Data Lake Storage (Gen 2): abfss://<file_system>@<account_name>.dfs.core.windows.net/<folder>/<file>
- Datastore: azureml://datastores/<datastore_name>/paths/<folder>/<file>

When you create a data asset and point to a file or folder stored on your local device, a copy of the file or folder will be uploaded to the default datastore workspaceblobstore.

**Create a URI file data asset**
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

my_path = '<supported-path>'

my_data = Data(
    path=my_path,
    type=AssetTypes.URI_FILE,
    description="<description>",
    name="<name>",
    version="<version>"
)

ml_client.data.create_or_update(my_data)