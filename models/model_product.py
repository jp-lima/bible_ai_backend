from os import stat
from pydantic import BaseModel

class Request_create_product(BaseModel):
    name:str
    price:float
    image_url:str
    type:str
    material:str
    authorization:str

class Request_update_product(BaseModel):
    product_id:str
    name:str | None = None
    price:float | None = None
    image_url:str | None = None
    authorization:str
    type: str | None = None
    material:str | None = None
    status:str | None = None

class Request_delete_product(BaseModel):
    product_id:str
    authorization:str
