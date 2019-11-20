from setuptools import setup

setup(
    name='skybucket',
    version='1.0',
    author='Pawel Fraczyk',
    author_email='pawel@fraczyk.eu',
    description='Skybucket allows to setup static website on AWS with S3, Route53 and CloufFront.',
    license='GPLv3+',
    packages=['skybucket'],
    url='https://github.com/pawelfraczyk/automating-aws-python',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        skybucket=skybucket.skybucket:cli
        '''
)