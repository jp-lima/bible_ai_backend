from fastapi import APIRouter

from service.subscription_service import *
from service.subscription_service import service_create_subscription     


router = APIRouter(
prefix="/subscription",
tags=["subscription"]
        )
 

@router.get("")
def get_subscription():


    return "Run subscription"

@router.post("")
def create_new_subscription():

   response = service_create_subscription() 

   return response







