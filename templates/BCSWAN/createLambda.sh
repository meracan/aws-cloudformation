
ZIPFILE=s3netcdfapi.zip

rm -R lambda
mkdir lambda
cd lambda
cp -r ../../../../s3-netcdf-api/s3netcdfapi/*.py .
cp -r ../../../../s3-netcdf/s3netcdf .
cp -r ../../../../binary-py/binarypy .

pip install --no-deps -t . netcdf4 
# rm -R ./numpy* # Don't need numpy since we are using a lambda layer
# rm -R /bin # Don't need numpy since we are using a lambda layer
# rm -R ./*dist-info


find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
# zip -r ../$PACKAGE.zip *
# aws s3 cp ../$ZIPFILE s3://$AWS_TEMPLATES/lambda/function/$ZIPFILE
# cd ..
# rm -R lambda
# rm $ZIPFILE
# echo s3://$AWS_TEMPLATES/lambda/function/$ZIPFILE