import bcrypt 
"""Hash a password"""
def _hash_password(password:str):  
    password =b"password"
    hashed =bcrypt.hashpw(password,bcrypt.gensalt())
    return   hashed 