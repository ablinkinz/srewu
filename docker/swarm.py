import docker
import os
import subprocess
client = docker.from_env()

'''
Initalize Docker on Minion as a Swarm Manager
NOTE *** there are 5


'''


def swarm_init(advertise_addr=str,listen_addr=int, force_new_cluster=bool ):
    client.swarm.init(advertise_addr, listen_addr,force_new_cluster)
    print('Docker swrarm has been Initalized on the minion')
    print('Worker Join token below!')
    os.system("docker swarm join-token worker | xargs | awk '{print $16}' ")

#swarm_init(advertise_addr='ens4',listen_addr='0.0.0.0:5000', force_new_cluster=False)

