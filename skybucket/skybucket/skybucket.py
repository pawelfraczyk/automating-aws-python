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

import mimetypes
from pathlib import Path

import click

import boto3
from botocore.exceptions import ClientError

session = boto3.Session(profile_name='awsPython')
s3 = session.resource('s3')


@click.group()
def cli():
    """Webotron deploys websites to AWS."""
    pass


@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets."""
    for bucket in s3.buckets.all():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in a bucket."""
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure S3 Bucket."""
    s3_bucket = None
    try:
        s3_bucket = s3.create_bucket(
            Bucket=bucket,
            CreateBucketConfiguration={
                'LocationConstraint': session.region_name}
            )
    except ClientError as err:
        if err.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            s3_bucket = s3.Bucket(bucket)
        else:
            raise err
    policy = """
    {
    "Version":"2012-10-17",
    "Statement":[
        {
        "Sid":"PublicRead",
        "Effect":"Allow",
        "Principal": "*",
        "Action":["s3:GetObject"],
        "Resource":["arn:aws:s3:::%s/*"]
        }
    ]
    }
    """ % s3_bucket.name
    policy = policy.strip()
    pol = s3_bucket.Policy()
    pol.put(Policy=policy)
    s3_bucket.Website().put(WebsiteConfiguration={
        'ErrorDocument': {
            'Key': 'error.html'
        },
        'IndexDocument': {
            'Suffix': 'index.html'
        }
    })

    return


def upload_file(s3_bucket, path, key):
    """Upload path to s3_bucket at key."""
    content_type = mimetypes.guess_type(key)[0] or 'text/plain'

    s3_bucket.upload_file(
        path,
        key,
        ExtraArgs={
            'ContentType': content_type
        }
    )


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync the content of website to bucket."""
    s3_bucket = s3.Bucket(bucket)

    root = Path(pathname).expanduser().resolve()

    def handle_directory(target):
        for p in target.iterdir():
            if p.is_dir():
                handle_directory(p)
            if p.is_file():
                upload_file(
                    s3_bucket, str(p), str(p.relative_to(root)))

    handle_directory(root)


if __name__ == '__main__':
    cli()
