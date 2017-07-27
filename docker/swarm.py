import docker

client = docker.from_env()

'''
Initalize Docker on Minion as a Swarm Manager
NOTE *** there are 5


'''


def swarm_init(advertise_addr=str,listen_addr=int, force_new_cluster=bool ):
    client.swarm.init(advertise_addr, listen_addr,force_new_cluster).logs()
    print('Docker swrarm has been Initalized on the minion')


swarm_init(advertise_addr='ens4',listen_addr='0.0.0.0:5000', force_new_cluster=False)

#def swarm_join(remote_addrs=list, join_token=str, advertise_addr=str):
