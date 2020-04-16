# Telemac Examples
Review environment variables and run.

**basic**
Basic Telemac services.
It includes a new bucket and two dynamodb tables(cas,data).
```bash
export AWS_STACKNAME=$AWS_PROJID-telemac-basic
export AWS_BUCKETNAME=$AWS_PROJID-basic
aws cloudformation create-stack 
  --stack-name $AWS_STACKNAME  
  --template-url "https://$AWS_TEMPLATES.s3.amazonaws.com/templates/telemac/basic.yaml" 
  --parameter-overrides BucketTemplateName=$AWS_TEMPLATES BucketName=$AWS_BUCKETNAME
```
