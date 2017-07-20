import boto3

def ec2_details():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    data = response['Reservations']
    for item in data:
        for items in item['Instances']:
            InstanceId = items['InstanceId']
            DnsName = items['PublicDnsName']
            PublicIP = items['PublicIpAddress']
            PrivateIP = items['PrivateIpAddress']
            print ("instance = " + InstanceId + ", " "DNS Name = " + DnsName + ", " + "Public IP = " + PublicIP + ", " + "Private IP = " + PrivateIP)

ec2_details()