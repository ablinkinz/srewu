import docker
import os
import subprocess
import salt.config
import salt.loader
__opts__ = salt.config.minion_config('/etc/salt/minion')
__grains__ = salt.loader.grains(__opts__)
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




def swarm_join(join_token=str,remote_addrs=list,listen_addr=str):
    d = []
    client.swarm.join(join_token,remote_addrs,listen_addr)
    



swarm_join(join_token="SWMTKN-1-3mnh7j1k8ux3m6nsjhy88q3hjdgfse6y3alcpcszojg2c2eq16-2d0d0q38l6a4yyeaeuorxk54v",remote_addrs=("10.142.0.2:2377"],listen_addr="ens4")
