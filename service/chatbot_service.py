from locale import windows_locale
import re

from requests import status_codes
from integrations.groq import integration_groq 
from repositories.wallet_repo import get_one_wallet_by_uuid, put_value_in_wallet_by_user_id  
from fastapi.responses import JSONResponse

def chatbot_message_service(user_id:str, prompt:str,religion:str,mood:str,need:str, historic:list ):

    wallet = get_one_wallet_by_uuid(user_id)  

    if wallet[0]["balance"] == 0:

        return JSONResponse(status_code=429, content="Você atingiu o limite de créditos do seu plano" )


    put_value_in_wallet_by_user_id(wallet[0]["balance"]- 1, user_id) 
            
    message = integration_groq(prompt, religion, need, mood, historic) 

    return message
    







