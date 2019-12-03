# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-2:439352748066:handleLabelDetectionTopic:28938402-c724-46df-b6db-bb9e41905a9a', 'Sns': {'Type': 'Notification', 'MessageId': '77f45776-d5a3-5c05-ac57-0116590a111c', 'TopicArn': 'arn:aws:sns:us-east-2:439352748066:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"a022e7552a16dd529da189c54c6f74bd9baaa6a04f701f7ad668d35c8eb0cc6d","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1575389800930,"Video":{"S3ObjectName":"video.mp4","S3Bucket":"rekoclip-video-analyzer2"}}', 'Timestamp': '2019-12-03T16:16:41.041Z', 'SignatureVersion': '1', 'Signature': 'eIZnd2oCZbdepZkyFq599CpfqkUcQ3jm1enbVxfB0Niu/b661ED0sUa4VmeX9TqQDGg0Nwd5Rdy9Bef2dMaPYDoPoVHiimHtHcd5h73SnOeqVFUfHIPE7x9iWMA9cVuGCTNpwEJ0kSdt+PwZpejA88z2FhD/YuEVeZmITBndDl5kUZ+ApDibHhAo806CuEalWa4jXoa8ltTHadeBVyJTWa6wBxNyfAE21D+Zcm7untw8Ag3mt5vxX45BmRbrljczEm7aDRSc4uoJUTJuk81RbAbQXtTE1lDJ573ojTkJcR2P5iktGLPpFApU8inHvICw/dslF84H74XaYue0ZR6r+Q==', 'SigningCertUrl': 'https://sns.us-east-2.amazonaws.com/SimpleNotificationService-6aad65c2f9911b05cd53efda11f913f9.pem', 'UnsubscribeUrl': 'https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:439352748066:handleLabelDetectionTopic:28938402-c724-46df-b6db-bb9e41905a9a', 'MessageAttributes': {}}}]}
event.keys()
event['Records'][0]
event['Records'][0].keys()
event['Records'][0]['Sns']['Message']
import json
json.loads(event['Records'][0]['Sns']['Message'])
