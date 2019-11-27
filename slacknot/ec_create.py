# coding: utf-8
import boto3 
session = boto3.Session(profile_name='awsPython')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    

import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)

ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-922914f7')
img.name
ami_name = 'amzn-ami-hvm-2018.03.0.20180508-x86_64-gp2'
filter = [{'Name': 'name', 'Values': [ami_name]}]
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
ec2.Instances
ec2.Instance(id='i-0c974a90edf1cd0f9')
inst.terminate()
ec2.Instance(id='i-0c974a90edf1cd0f9').terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst= instances[0]
inst.wait_until_running()
inst.reload()
inst.public_dns_name

inst.security_groups
# Look up the security group
# Authorize incoming connections on SSH port to the security group
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])

sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
