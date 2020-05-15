cd $(dirname $0)

zip -r ../meracanapi.zip *
aws s3 cp ../meracanapi.zip s3://$AWS_TEMPLATES/lambda/function/meracanapi.zip


aws s3 cp path/to/datafolder  s3://uvic-bcwave/devdata --recursive --profile primed-admin
