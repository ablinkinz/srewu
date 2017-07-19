import boto3
import json

'''
Returns Running instances
'''

def instances_running():
    recource = []
    client = boto3.client('ec2')
    nodes = client.describe_instances()
    data = nodes['Reservations']
    for item in data:
        for items in item['Instances']:
            DNSname = items['PublicDnsName']
            InstanceId = items['InstanceId']
            data = InstanceId
            recource.append(data)
    return recource

server = instances_running()

def pass_along():
     for item in server:
          return item
