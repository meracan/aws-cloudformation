# AWS Cloudformation for MERACAN
AWS Cloudformation templates for Marine Energy Resource Assessment Canada.

## Installation
```bash
# Set environment variable - AWS_TEMPLATES
export AWS_TEMPLATES=meracan-templates

# Create template bucket
aws cloudformation deploy --stack-name $AWS_TEMPLATES --template-file templates/s3/basic.yaml --parameter-overrides BucketName=$AWS_TEMPLATES
```



s3://meracan-templates/lambda/function/meracanapi.zip arn:aws:lambda:us-east-1:440480703237:layer:meracanapi:3