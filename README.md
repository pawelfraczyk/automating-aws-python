# automating-aws-python
Repository for automating AWS with Python

## 01-skybucket

SkyBucket is a script that will sync a local directory to an s3 bucket, and optionally configure Route 53 and CloudFront as well.

### Features

SkyBucket currently has the following features:

- List bucket
- List objects of bucket
- Create and setup s3 bucket
- Sync directory tree to the bucket
- Set AWS profile --profile=<profile_name>
- Configure Route 53 domain
- Set up CloufFront Distribution with SSL

## 02-slacknot

Slacknot is an app to notify team on Slack about changes to your AWS account using CloudWatch events.

### Features

Currently features of Slacknot:

- Send notifications to Slack when CloudWatch event happen.