# automating-aws-python
Repository for automating AWS with Python

## 01-web

SkyBucket is a script that will sync a local directory to an s3 bucket, and optionally configure Route 53 and CloudFront as well.

### Features

SkyBucket currently has the following features:

- List bucket
- List objects of bucket
- Create and setup s3 bucket
- Sync directory tree to the bucket
- Set AWS profile --profile=<profile_name>