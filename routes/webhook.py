from os import stat
from models.webhook import * 
from fastapi import APIRouter,Form,File, UploadFile,Response, HTTPException
 
router = APIRouter(
prefix="/webhook",
tags=["webhooks"]
        )
   
@router.post("/asaas")
def webhook(data: dict):
    print(data)
    return  





