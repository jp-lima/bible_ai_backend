from pydantic import BaseModel 


class Request_send_message(BaseModel):
    prompt:str 
    user_id:str 
    religion:str  
    need:str 
    mood:str 

    



