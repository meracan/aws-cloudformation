
aws cloudformation deploy \
  --template-file api.yaml \
  --stack-name $STACKNAME \
  --parameter-overrides BucketName=bucket \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation describe-stacks --stack-name $STACKNAME > output.json
