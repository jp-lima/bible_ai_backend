from fastapi import APIRouter

from service.subscription_service import *
from models.model_subscription import *


router = APIRouter(
prefix="/subscription",
tags=["subscription"]
        )
 

@router.get("")
def get_subscription():
    subscriptions = get_all_subscriptions() 

    return subscriptions

@router.post("")
def create_new_subscription(request: Request_new_subscription):

   response = service_create_subscription(request.user_id, request.plan_id, request.user_cpf, request.billing_type, request.user_name, request.cycle) 

   return response







