# Examples

```bash
export AWS_TEMPLATES=meracan-templates
```

#### Meracan-api
```bash
aws cloudformation deploy \
  --template-file templates/meracan-api/test.yaml \
  --stack-name testmeracanapi \
  --parameter-overrides BucketName="1" \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation describe-stacks --stack-name testmeracanapi  
  
```

#### Meracan-api-2
```bash
aws cloudformation deploy \
  --template-file templates/meracan-api/test2.yaml \
  --stack-name testmeracanapi3 \
  --parameter-overrides BucketName="1" APILayer="arn:aws:lambda:us-east-1:440480703237:layer:meracanapi:3" \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

```


#### Basic
```bash
export AWS_STACKNAME=cognitotest && \
aws cloudformation deploy \
  --template-file basic.yaml \
  --stack-name $AWS_STACKNAME \
  --parameter-overrides ApiRole=API \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

#### Roles
```bash
export AWS_STACKNAME=cognitoroles && \
aws cloudformation deploy \
  --template-file roles.yaml \
  --stack-name teststack1 \
  --parameter-overrides BucketTemplateName=meracan-templates ApiRole=api \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

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

# API LAMBDA
Basic cloud formation for Api Gateway and Lambda.



#### Roles
```bash
export AWS_STACKNAME=cognitoroles && \
aws cloudformation deploy \
  --template-file roles.yaml \
  --stack-name teststack1 \
  --parameter-overrides BucketTemplateName=meracan-templates ApiRole=api \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

# Telemac Examples
Review environment variables and run.

### Basic

Basic Telemac services.
It includes a new bucket and two dynamodb tables(cas,data).
```bash
export $AWS_PROJID="meracan-awscloud-telemac-basic"
export AWS_STACKNAME=$AWS_PROJID-telemac-basic
export AWS_BUCKETNAME=$AWS_PROJID
aws cloudformation create-stack 
  --stack-name $AWS_STACKNAME  
  --template-url "https://$AWS_TEMPLATES.s3.amazonaws.com/templates/telemac/basic.yaml" 
  --parameter-overrides BucketTemplateName=$AWS_TEMPLATES BucketName=$AWS_BUCKETNAME
```
