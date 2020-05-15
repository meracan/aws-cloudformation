## Lambda
To following commands "compile" node/python lambda function and upload to S3.
Make sure environment variable `AWS_TEMPLATES` is specified.
Lambda-layers are directly uploaded to AWS.

```bash
# Mercan-api
bash layer/meracanapi/run.sh

# apipython
bash function/meracanapi/run.shc
```