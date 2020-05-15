import json
import os
with open('output.json') as file:
  data = json.load(file)
obj={}

for item in data['Stacks'][0]['Outputs']:
  obj[item['OutputKey']]=item['OutputValue']  

activate=os.path.join(os.environ.get("CONDA_PREFIX"),"etc/conda/activate.d")
pathActivate=os.path.join(activate,"env_vars.sh")
os.makedirs(activate, exist_ok=True)
with open(pathActivate,"a+") as file:
  file.write("export AWS_BUCKETNAME={}\n".format(obj['S3BUCKET']))
  file.write("export AWS_TABLECAS={}\n".format(obj['TABLECAS']))
  file.write("export AWS_TABLEDATA={}\n".format(obj['TABLEDATA']))
  file.write("export AWS_USERPOOLID={}\n".format(obj['USERPOOLID']))
  file.write("export AWS_USERPOOLCLIENTID={}\n".format(obj['USERPOOLCLIENTID']))
  file.write("export AWS_ROLEADMIN={}\n".format(obj['ROLEADMINARN']))
  file.write("export AWS_API={}\n".format(obj['AWSAPI']))


deactivate=os.path.join(os.environ.get("CONDA_PREFIX"),"etc/conda/deactivate.d")
pathDeactivate=os.path.join(deactivate,"env_vars.sh")
os.makedirs(deactivate, exist_ok=True)
with open(pathDeactivate,"a+") as file:
  file.write("unset AWS_BUCKETNAME\n")
  file.write("unset AWS_TABLECAS\n")
  file.write("unset AWS_TABLEDATA\n")
  file.write("unset AWS_USERPOOLID\n")
  file.write("unset AWS_USERPOOLCLIENTID\n")
  file.write("unset AWS_ROLEADMIN\n")
  file.write("unset AWS_API\n")