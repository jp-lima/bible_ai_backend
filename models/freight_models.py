from pydantic import BaseModel


class Request_Create_Freight(BaseModel):
    authorization:str
    state:str
    city:str | None = None 
    value:float











