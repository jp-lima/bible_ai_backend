from os import stat
from models.webhook import * 
from fastapi import APIRouter,Form,File, UploadFile,Response, HTTPException
from service.webhook_service import *
 
router = APIRouter(
prefix="/webhook",
tags=["webhooks"]
        )
   
@router.post("/asaas")
def webhook(data: dict):

    response =  receive_payment_from_webhook(data)

    return response    





