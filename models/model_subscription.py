from pydantic import BaseModel


class Request_new_subscription(BaseModel):
    user_name:str
    user_id:str
    plan_id:str
    billing_type:str # CREDIT_CARD, PIX, BOLETO, UNDEFINED
    user_cpf:str
    cycle:str # monthly, quartely, semiannualy     







