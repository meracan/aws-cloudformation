## Nested cloudformation templates
Cloudformation templates needs to be stored in a S3 bucket.
It currently does not allow Github (or other) URL links when using [nested cloudformation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html). 
`{AWS_TEMPLATES}` needs to be changed to an unique Bucket Id.

```bash
# Copy repo
# Set environment variable - AWS_TEMPLATES
export AWS_TEMPLATES=meracan-templates

# Create template bucket
aws cloudformation deploy --stack-name $AWS_TEMPLATES --template-file ../s3/basic.yaml --parameter-overrides BucketName=$AWS_TEMPLATES

# Upload all templates 
aws s3 cp ../../ s3://$AWS_TEMPLATES/ --recursive --exclude "*" --include "*.yaml"
```

Next is to run another cloudformation as shown in the `/nested.yaml`.
```bash
aws cloudformation deploy \
  --template-file basic.yaml \
  --stack-name "Demo-Nested" \
  --parameter-overrides BucketTemplateName=$AWS_TEMPLATES BucketName=NewBucket \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```