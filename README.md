# AWS Cloudformation for MERACAN
AWS Cloudformation templates for Marine Energy Resource Assessment Canada.

## Installation

Cloudformation templates needs to be stored in a S3 bucket.
It currently does not allow Github (or other) URL links when using [nested cloudformation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html). 
`{AWS_TEMPLATES}` needs to be changed to an unique Bucket Id.

To copy all cloudformation templates:
```bash
# Copy repo
git clone https://github.com/meracan/aws-cloudformation.git
cd aws-cloudformation

# Set environment variable - AWS_TEMPLATES
export AWS_TEMPLATES=meracan-templates

# Create bucket
aws cloudformation deploy --stack-name $AWS_TEMPLATES --template-file s3/bucket.yaml --parameter-overrides BucketName=$AWS_TEMPLATES

# Update bucket
aws s3 cp . s3://$AWS_TEMPLATES/ --recursive --exclude "*" --include "*.yaml"
```

### Testing
Set `AWS_PROJID` to be able to run any examples.
```bash
export AWS_PROJID=meracan
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