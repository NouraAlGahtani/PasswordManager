import hashlib

class PassowrdManager:
 def __init__(self):
  self.passwords = {}
  
  
  
   # ADD FUNCTION  
    #Make sure ur Attribtes are lowerCased!
  def  add_Password(self, website,username,password):
    hashed_password = 
    hashlib.sha256(password.encode()).hexdigest()
    if website in self.passwords:
        self.passwords[website][username] = hashed_password
    else:
        self.password[website] = {username: hashed_password}
    
    

        