from os import stat
from models.webhook import * 
from fastapi import APIRouter,Form,File, UploadFile,Response, HTTPException


router = APIRouter(
prefix="/webhook",
tags=["webhook-yampi"]
        )
   
@router.post("/mercadopago")
def webhook(data: dict):
   
    return  





