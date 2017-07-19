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
    for item in clean['Tags']:
            g = []
            node = item['ResourceId']
            key = item['Key']
            value = item['Value']
            d = {'server': node, 'Tag_Key': key, 'Value': value}
            if d['Tag_Key'] == 'Name' and d['Value'] == "":
                g.append(d['server'])
                client.create_tags(Resources=g,Tags=[{'Key': 'Warning_Tag','Value':'IN 48 HRS DELETETION WILL HAPPEN UNLESS CORRECT TAGS ARE APPLIED'}])


ec2_intance_tags_check(node)
