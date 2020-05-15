from meracanapi import Cognito


if __name__ == "__main__":
  cognito=Cognito()
  
  cognito.admin_create_user(
      Username="admin",
      TemporaryPassword= "P@ssw0rdAdmin",
      ForceAliasCreation= True ,
      MessageAction= 'SUPPRESS'
  )
  
  cognito.admin_set_user_password(
    Username='admin',
    Password='P@ssw0rdAdmin',
    Permanent=True
  )
  
  cognito.admin_add_user_to_group(Username="admin",GroupName="Admin")