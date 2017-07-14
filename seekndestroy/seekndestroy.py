import boto3
import json



#session = boto3.Session(profile_name='default')

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


def instances_Running_Status():
    client = boto3.client('ec2')
    for item in instances_running():
        output = client.describe_instance_status(InstanceIds=[item])
        print output


def ec2_intance_tags_check():
    client = boto3.client('ec2')
    response = client.describe_tags(Filters=[{'Name': 'resource-type','Values': ['instance']}])
    for item in response['Tags']:
        print item



ec2_intance_tags_check()

    #if item['Value'] == '':
    #        no_tag_ec2 = item['ResourceId']
    #        print no_tag_ec2
            #client.create_tags(Resources=[no_tag_ec2],Tags=[{'Key': 'Warning_Tag','Value':'48_HRS_DELETETION_WILL_HAPPEN_UNLESS_CORRECT_TAGS_ARE_APPLIED'}])
    
