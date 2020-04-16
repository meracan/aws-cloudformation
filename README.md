# AWS Cloudformation for MERACAN
Desc.

## Installation

An unique project Id `{Name}` needs to be created. The project Id is used as s3 bucket name.
The code below creates a bucket for templates and copy all local templates from `aws-cloudformation` to the bucket. 
This is necessary to perform [nested cloudformation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html) in aws.

```bash

git clone https://github.com/meracan/aws-cloudformation.git
cd aws-cloudformation

export AWS_PROJID=meracantest1
aws cloudformation deploy --stack-name $AWS_PROJID-bucket --template-file s3/bucket.yaml --parameter-overrides BucketName=$AWS_PROJID
aws s3 cp . s3://$AWS_PROJID/templates/ --recursive --exclude "*" --include "*.yaml"
```

### Telemac
```bash
aws cloudformation deploy --stack-name $AWS_PROJID-telemac --template-file telemac/simple.yaml --parameter-overrides BucketName=$AWS_PROJID
```



## DynamoDB Testing
```bash
# Create stack
aws cloudformation deploy --stack-name TestDynamoDBTable --template-file table.yaml --parameter-overrides TableName=TestTable HashKeyElementName=id
aws cloudformation deploy --stack-name TestDynamoDBTableCAS --template-file aws-cloudformation/dynamodb/tableCas.yaml --parameter-overrides TableName=TestTableCas
aws cloudformation deploy --stack-name TestDynamoDBTableDATA --template-file aws-cloudformation/dynamodb/tableData.yaml --parameter-overrides TableName=TestTableData

# Delete stack
aws cloudformation delete-stack --stack-name TestDynamoDBTable
aws cloudformation delete-stack --stack-name TestDynamoDBTableCAS
aws cloudformation delete-stack --stack-name TestDynamoDBTableDATA
```

## S3 Testing
```bash
aws cloudformation deploy --stack-name TestS3Bucket --template-file aws-cloudformation/s3/bucket.yaml --parameter-overrides BucketName=mercantest
aws cloudformation delete-stack --stack-name TestS3Bucket
```