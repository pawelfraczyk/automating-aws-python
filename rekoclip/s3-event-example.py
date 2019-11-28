# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-2', 'eventTime': '2019-11-28T11:23:08.221Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDAWMS3W5AREP2FOJKHQ'}, 'requestParameters': {'sourceIPAddress': '89.64.42.40'}, 'responseElements': {'x-amz-request-id': 'A8F0758CA1CA9016', 'x-amz-id-2': '3agSquVCd0npaWpKcR+8NlJG+s4PLX1p79voMnJLSEOMIhnBSv2Jm+LCztP5YHU+1VJzGBnjmJ4='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'c7bd6cdb-60ff-486d-81f8-5a22bdb8410e', 'bucket': {'name': 'rekoclip-video-analyzer2', 'ownerIdentity': {'principalId': 'A3DKLSSWXKZOLY'}, 'arn': 'arn:aws:s3:::rekoclip-video-analyzer2'}, 'object': {'key': 'video2.mp4', 'size': 3598161, 'eTag': 'bbc5379e6a8dd9ef5f20fec0cbb14e5f', 'sequencer': '005DDFAE13F772C3FE'}}}]}
event
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
