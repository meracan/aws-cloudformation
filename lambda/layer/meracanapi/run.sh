cd $(dirname $0)
rm -R python
mkdir -p python/lib/python3.8/site-packages
pip install -t python/lib/python3.8/site-packages ~/environment/meracan-api
zip -r ../meracanapi.zip *
aws lambda publish-layer-version \
    --layer-name meracanapi \
    --description "Mercan-api" \
    --license-info "MIT" \
    --zip-file fileb://../meracanapi.zip \
    --compatible-runtimes python3.6 python3.7 python3.8