# AWS Service Installation
These are steps to create AWS services such as DynamoDB, S3, Api Gateway, etc. using CloudFormation.

## Pre-Installation
If conda evnironment `meracan` is not created, please follow the steps [here](../README.md) and activate the environment `conda activate meracan`.
The Lambda function needs to be stored in a S3 bucket since CloudFormation only allows function from S3.
The name of the bucket needs to be set as environment variable: `export AWS_TEMPLATES=meracan-templates`, before using CloudFormation.

#### (Optional) Create S3 Bucket(AWS_TEMPLATES)
If `AWS_TEMPLATES` bucket does not exist:
```bash
aws s3api create-bucket --bucket $AWS_TEMPLATES --region us-east-1
```

#### Upload Lambda function to S3
```bash
bash createLambda.sh
```
Check and review `s3://meracan-templates/lambda/function/meracanapi.zip` in `api.yaml` file.

## Installation
Create AWS services using the `STACKNAME` environment variable. This will generate an output.json with all the services id.
```bash
export STACKNAME=testmeracanapi3
bash createAWS.sh 
```

## Post-Installation
Save environment variables to conda's environment
```bash
python extract.py
conda deactivate
conda activate meracan
```
Here's the list of environment variables:
- `AWS_BUCKETNAME`
- `AWS_TABLECAS`
- `AWS_TABLEDATA`
- `AWS_USERPOOLID`
- `AWS_USERPOOLCLIENTID`
- `AWS_ROLEADMIN`
- `AWS_API`

#### Create testing users
To is to test the lambda function.
```bash
bash createUsers.py
```



## (For development) - Review environment variables
To modify conda's environment vairables:
```bash
conda activate meracan
vi $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
vi $CONDA_PREFIX/etc/conda/deactivate.d/env_vars.sh
```