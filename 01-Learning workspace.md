# Azure ML Resource Notes

**Azure ML Resources**
- The workspace
- Compute resources
- Datastores

**Azure ML Assets**
- Models
- Environments
- Data
- Components

- *Note* When a workspace is created, an __Azure Storage account__ is created and automatically connected to the workspace. you have four datastores already added to your workspace:

**workspaceartifactstore:** Connects to the azureml container of the Azure Storage account created with the workspace. Used to store __compute and experiment logs__ when running jobs.
**workspaceworkingdirectory:** Connects to the file share of the Azure Storage account created with the workspace used by the __Notebooks__ section of the studio. Whenever you upload files or folders to access from a compute instance, it's uploaded to this file share.
**workspaceblobstore:** Connects to the __Blob Storage__ of the Azure Storage account created with the workspace. Specifically the azureml-blobstore-... container. Set as the default datastore, which means that whenever you create a data asset and upload data, it's stored in this container.
**workspacefilestore:** Connects to the __file share__ of the Azure Storage account created with the workspace. Specifically the azureml-filestore-... file share.

**Models va Artifacts**

Any file generated (and captured) from an experiment's run or job is an artifact.
A model in MLflow is also an artifact. However:

- You can deploy them on real-time or batch endpoints without providing an scoring script nor an environment.
- When deployed, Model's deployments have a Swagger generated automatically and the Test feature can be used in Azure Machine Learning studio.
Models can be used as pipelines inputs directly.
You can use the Responsible AI dashbord (preview).

**Environments**
- An environment is stored as __an image in the Azure Container Registry__ created with the workspace when it's used for the first time. Whenever you want to run a script, you can specify the environment that needs to be used by the compute target.

**Components**
- To make it easier to share code, you can create a component in a workspace. 

# Train models in the workspace

To train models with the Azure Machine Learning workspace, you have several options:

- Use Automated Machine Learning.
- Run a Jupyter notebook.
- Run a script as a job.

There are different types of jobs depending on how you want to execute a workload:

- Command: Execute a single script.
- Sweep: Perform hyperparameter tuning when executing a single script.
- Pipeline: Run a pipeline consisting of multiple scripts or components.

