#!/usr/bin/python
# -*- coding: utf-8 -*-

"""SkyBucket: Deploy websites with aws.

SkyBucket automates the process of deploying static websites to AWS.
- Configure AWS S3 Buckets
    - Create bucket
    - Change properties to static website hosting
    - Sync local files to the bucket
- Configure DNS with AWS Route 53
- Configure a  Content Delivery Network and SSL with CloudFront
"""

import click

import boto3
from bucket import BucketManager

session = boto3.Session(profile_name='awsPython')
bucket_manager = BucketManager(session)


@click.group()
def cli():
    """Webotron deploys websites to AWS."""
    pass


@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets."""
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in a bucket."""
    for obj in bucket_manager.all_objects(bucket):
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure S3 Bucket."""
    s3_bucket = bucket_manager.create_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)

    return


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync the content of website to bucket."""
    bucket_manager.sync(pathname, bucket)


if __name__ == '__main__':
    cli()
