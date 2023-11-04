from azureml.core import Workspace, Experiment,Environment,ScriptRunConfig

ws=Workspace.from_config()
experiment=Experiment(workspace=ws,name='experiment_hello_worlds')
config=ScriptRunConfig(source_directory='.',script='hello.py',compute_target='meincluster')
run=experiment.submit(config)
aml_url=run.get_portal_url()
print(aml_url)