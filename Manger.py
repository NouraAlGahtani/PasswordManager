import hashlib

class PassowrdManager:
 def __init__(self):
  self.passwords = {}
  
  
  
   #----------------- ADD FUNCTION--------------------------------------------- 
   
    #Make sure ur Attribtes are lowerCased!
  def  add_Password(self, website,username,password):
    hashed_password = ""
    hashlib.sha256(password.encode()).hexdigest()
    if website in self.passwords:
        self.passwords[website][username] = hashed_password
    else:
        self.password[website] = {username: hashed_password}
        
        
# ----------------------RETRIVE FUNCTION---------------------------------------
  def get_Password(self, website, username):
    if website in self.passwords and username in self.passwords[website]:
        return self.passwords[website][username]
    else:
        return None 
    print("UserName invaild")
#---------------------------DELETE FUNCTION-------------------------------------
def delete_password(self,website,username):
    if website in self.passwords and username in self.passwords[website]:
        del self.
    

        