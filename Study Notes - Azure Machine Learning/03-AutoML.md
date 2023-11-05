# Preprocess data and configure featurization

<pre>
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import Input

my_training_data_input = Input(type=AssetTypes.MLTABLE, path="azureml:input-data-automl:1")
</pre>

**Create classsification automl job**

<pre>
from azure.ai.ml import automl

# configure the classification job
classification_job = automl.classification(
    compute="aml-cluster",
    experiment_name="auto-ml-class-dev",
    training_data=my_training_data_input,
    target_column_name="Diabetic",
    primary_metric="accuracy",
    n_cross_validations=5,
    enable_model_explainability=True
)
</pre>

**To see list of metrics:**
<pre>
from azure.ai.ml.automl import ClassificationPrimaryMetrics
 
list(ClassificationPrimaryMetrics)
</pre>

**Set limits to Automl**
<pre>classification_job.set_limits(
    timeout_minutes=60, 
    trial_timeout_minutes=20, 
    max_trials=5,
    enable_early_termination=True,
)</pre>

**Submit Automl sub and Monitor**

# submit the AutoML job

<pre>
returned_job = ml_client.jobs.create_or_update(
    classification_job
)

aml_url=returned_jub.studio_url
print(aml_url)
</pre>