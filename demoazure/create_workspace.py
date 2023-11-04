from azureml.core import Workspace

ws= Workspace.create(name='sdkworkspace',
                     subscription_id='888ba289-69f6-465a-83ec-097e040139e7',
                     resource_group='dp100',
                     create_resource_group=False,
                     location='germanywestcentral')
ws.write_config(path='.azureml')