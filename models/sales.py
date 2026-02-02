from enum import auto
from pydantic import BaseModel

class Request_new_sale(BaseModel):
    products_id:list
    amounts:list
    user_id:str
    user_cep:str
    sizes: str
    status: str | None = None
    state:str
    city:str
    neighboor:str
    street:str
    complement:str

class RequestCartById(BaseModel):
    authorization:str

class Request_put_sale(BaseModel):
    sale_id:str
    value:float | None = None
    amount:int | None = None
    user_cep:str | None = None
    authorization:str | None = None
    status: str | None = None
    sizes: str | None = None
    code: str | None = None
    state:str | None = None
    city:str | None = None
    neighboor:str | None = None
    street:str | None = None
    complement:str | None = None

class RequestCheckout(BaseModel):
    products_id:list









