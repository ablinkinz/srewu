import boto3
import runningec2 as running
import json
client = boto3.client('ec2')
node = running.pass_along


def ec2_intance_tags_check(node):
    client = boto3.client('ec2')
    response = client.describe_tags(Filters=[{'Name': 'resource-type','Values': ['instance']}])
    out = json.dumps(response)
    clean = json.loads(out)
    d = []
    try:
        for item in clean['Tags']:
            node = item['ResourceId']
            key = item['Key']
            value = item['Value']
            d = {'server': node, 'Tag_Key': key, 'Value': value}
            return d
    except:
        print "This is an error message!"



info = ec2_intance_tags_check(node)

for item in info:
    print item['Tag_Key']
