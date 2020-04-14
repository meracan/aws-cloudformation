

# DynamoDB cloudformation

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