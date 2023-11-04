from azureml.core import Workspace
from azureml.core.compute import ComputeTarget,AmlCompute
from azureml.core.compute_target import ComputeTargetException

ws=Workspace.from_config()

cpu_cluster_name='meincluster'

try:
    cluster_name=ComputeTarget(workspace=ws,name=cpu_cluster_name)
    print('cluster exists')
except:
    compute_config=AmlCompute.provisioning_configuration(vm_size='STANDARD_A1_V2',idle_seconds_before_scaledown=240,min_nodes=0,max_nodes=4)
    cpu_cluster=ComputeTarget.create(ws,cpu_cluster_name,compute_config)

cpu_cluster.wait_for_completion(show_output=True)