import docker
import os
import subprocess
client = docker.from_env()

'''
Initalize Docker on Minion as a Swarm Manager
* Does not work on Windows OS at the moment
salt <Target> advertise_addr='ens4' listen_addr='0.0.0.0:5000' force_new_cluster=False
'''


def swarm_init(advertise_addr=str,listen_addr=int, force_new_cluster=bool ):
    d = []
    client.swarm.init(advertise_addr, listen_addr,force_new_cluster)
    output =  'Docker swrarm has been Initalized on the minion and the worker Join token is below'
    command = "docker swarm join-token worker | xargs | awk '{print $16}' "
    token = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    key  = token.communicate()[0]
    d.append({'Comment': output, 'Worker_Token': key})
    return d 
     





