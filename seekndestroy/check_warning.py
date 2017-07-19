import boto3
import runningec2 as running
import json
import tags
client = boto3.client('ec2')
node = running.pass_along
client = boto3.client('ec2')


def get_list_of_warnings(node):
    response = client.describe_tags(Filters=[{'Name': 'resource-type','Values': ['instance']}])
    out = json.dumps(response)
    clean = json.loads(out)
    g = []
    for item in clean['Tags']:
        node = item['ResourceId']
        key = item['Key']
        value = item['Value']
        d = {'server': node, 'Tag_Key': key, 'Value': value}
        if d['Tag_Key'] == 'Warning_Tag':
            g.append(d['server'])
    return g

def delete_recource(server):
    delete_node = server
    response = client.terminate_instances(InstanceIds=delete_node,DryRun=False)

delete_recource(get_list_of_warnings(node))
