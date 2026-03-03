from pydantic import BaseModel




class Request_new_subscription(BaseModel):
    plan_id:str
    user_id:str







