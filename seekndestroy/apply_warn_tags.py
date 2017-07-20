import boto3
import json
client = boto3.client('ec2')
import logging


'''
Returns Running instances
'''

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


instances_running()

def pass_along():
     for item in server:
          return item


'''
Adds Warning Tag
'''

def ec2_intance_tags_check(node):
    response = client.describe_tags(Filters=[{'Name': 'resource-type','Values': ['instance']}])
    out = json.dumps(response)
    clean = json.loads(out)
    d = []
    for item in clean['Tags']:
        g = []
        node = item['ResourceId']
        key = item['Key']
        value = item['Value']
        d = {'server': node, 'Tag_Key': key, 'Value': value}
        if d['Tag_Key'] == 'Name' and d['Value'] == "":
            g.append(d['server'])
            client.create_tags(Resources=g,Tags=[{'Key': 'Warning_Tag','Value':'IN 48 HRS DELETETION WILL HAPPEN UNLESS CORRECT TAGS ARE APPLIED'}])
#ec2_intance_tags_check(pass_along())
