# coding: utf-8
import boto3
session = boto3.Session(profile_name='awsPython')
as_client = session.client('autoscaling')

as_client.execute_policy(AutoScalingGroupName='Slacknot Scaling Group', PolicyName='Scale Up')
