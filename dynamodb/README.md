# DynamoDB Examples
Review environment variables and run.

**basic**
Basic table
```bash
export AWS_STACKNAME=$AWS_PROJID-dynamodb-basic
export AWS_TABLENAME=$AWS_PROJID-basic

aws cloudformation create-stack 
  --stack-name $AWS_STACKNAME
  --template-url "https://$AWS_TEMPLATES.s3.amazonaws.com/templates/dynamodb/basic.yaml" 
  --parameter-overrides TableName=$AWS_TABLENAME
```

**basicCas**
```bash
export AWS_STACKNAME=$AWS_PROJID-dynamodb-basicCas
export AWS_TABLENAME=$AWS_PROJID-basicCas

aws cloudformation create-stack 
  --stack-name $AWS_STACKNAME
  --template-url "https://$AWS_TEMPLATES.s3.amazonaws.com/templates/dynamodb/basicCas.yaml" 
  --parameter-overrides TableName=$AWS_TABLENAME
```

**basicData**
```bash
export AWS_STACKNAME=$AWS_PROJID-dynamodb-basicData
export AWS_TABLENAME=$AWS_PROJID-basicData

aws cloudformation create-stack 
  --stack-name $AWS_STACKNAME
  --template-url "https://$AWS_TEMPLATES.s3.amazonaws.com/templates/dynamodb/basicData.yaml" 
  --parameter-overrides TableName=$AWS_TABLENAME
```
