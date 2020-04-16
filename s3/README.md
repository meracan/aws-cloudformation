# S3 Examples
Review environment variables and run.

**basic**
Basic bucket.
```bash
export AWS_STACKNAME=$AWS_PROJID-s3-basic
export AWS_BUCKETNAME=$AWS_PROJID-basic

aws cloudformation create-stack 
  --stack-name $AWS_STACKNAME
  --template-url "https://$AWS_TEMPLATES.s3.amazonaws.com/templates/telemac/basic.yaml" 
  --parameter-overrides BucketName=$AWS_BUCKETNAME
```
