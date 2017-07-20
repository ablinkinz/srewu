import boto3
import json
client = boto3.client('ec2')
import logging




def instances_running():
    recource = []
    client = boto3.client('ec2')
    nodes = client.describe_instances()
    data = nodes['Reservations']
    logging.debug('Checking for Ec2 servers')
    for item in data:
        for items in item['Instances']:
            DNSname = items['PublicDnsName']
            InstanceId = items['InstanceId']
            data = InstanceId
            recource.append(data)
    return  recource


somthing = instances_running()



def show_tags(ids):
    ec2 = boto3.resource('ec2')
    nodes = []
    for item in ids:
        environment_exist = False
        d = {}
        instance = ec2.Instance(item)
        d['Servers'] = instance.id
        l = []

        for items in instance.tags:
            tags = items
            value = tags['Value']
            key = tags['Key']
            if key == "Environment":
                environment_exist = True
            l.append(key)
            l.append(value)
            d['AWS_KEY'] = l
        if not environment_exist:
            nodes.append(d['Servers'])
    return nodes


nodes = show_tags(somthing)


for server in nodes:
    print server
