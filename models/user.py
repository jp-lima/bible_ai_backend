from pydantic import BaseModel
from utils import password

class UserRequestLogin(BaseModel):
    email:str
    password:str
    
class UserCreateRequest(BaseModel):
    name:str
    email:str
    password:str
    phone:str

class UserDeleteRequest(BaseModel):
    user_id:str
    authorization:str

class RequestGetAuthorization(BaseModel):
    authorization:str

class RequestNewPassword(BaseModel):
    authorization:str
    new_password:str

class RequestPutUser(BaseModel):
    user_id:str
    authorization: str 
    email: str | None = None 
    user_name: str | None = None
    phone: str | None = None
    password: str | None = None
    




