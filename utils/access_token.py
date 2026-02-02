from dotenv import load_dotenv
import os
import jwt
import datetime

load_dotenv()

secret_key = os.getenv("SECRET_KEY")

def create_access_token(uuid:str,name:str,role:str):

    payload = {
        "sub":uuid,
        "name":name,
        "role":role,
            }

    token = jwt.encode(payload, str(secret_key), algorithm="HS256")
        

    return {"token":token,"type":"bearer" }

def decode_access_token(access_token:str):

    token_decoded =  jwt.decode(access_token,str(secret_key),algorithms=["HS256"])
    
    return token_decoded




if __name__ == "__main__":

   token = create_access_token("d9a2142f-16cf-4d20-bd4c-bcc371ec63b2", "João Pedro Lima", "user") 

   print("SECRET_KEY:", repr(secret_key))
   infos = decode_access_token(token["token"])

   print(infos)

