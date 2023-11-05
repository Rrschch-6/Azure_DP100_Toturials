There are two options to track machine learning jobs with MLflow:

- Enable autologging using mlflow.autolog()
- Use logging functions to track custom metrics using mlflow.log_


Before you can use either of these options, you need to set up the environment to use MLflow.

To use MLflow during training job, the *mlflow* and *azureml-mlflow* pip packages need to be installed on the compute executing the script. 

To enable autologging, add the following code to your training script:

<pre>
import mlflow

mlflow.autolog()
</pre>

Log metrics with MLflow
In your training script, you can decide whatever custom metric you want to log with MLflow.

Depending on the type of value you want to log, use the MLflow command to store the metric with the experiment run:

- mlflow.log_param(): Log single key-value parameter. Use this function for an input parameter you want to log.
- mlflow.log_metric(): Log single key-value metric. Value must be a number. Use this function for any output you want to store with the run.
- mlflow.log_artifact(): Log a file. Use this function for any plot you want to log, save as image file first.

<pre>
import mlflow

reg_rate = 0.1
mlflow.log_param("Regularization rate", reg_rate)
</pre>

# View the metrics in the Azure Machine Learning studio
When your job is completed, you can review the logged parameters, metrics, and artifacts in the Azure Machine Learning studio.

When you review job runs in the Azure Machine Learning studio, you'll explore a job run's metrics, which is part of an experiment.

To view the metrics through an intuitive user interface, you can:

1- Open the Studio by navigating to https://ml.azure.com.
2- Find your experiment run and open it to view its details.
3- In the Details tab, all logged parameters are shown under Params.
4- Select the Metrics tab and select the metric you want to explore.
5- Any plots that are logged as artifacts can be found under Images.
6- The model assets that can be used to register and deploy the model are stored in the models folder under Outputs + logs.