from locale import windows_locale
import re
from integrations.groq import integration_groq 
from repositories.wallet_repo import get_one_wallet_by_uuid, put_value_in_wallet_by_user_id  

def chatbot_message_service(user_id:str, prompt:str,religion:str,mood:str,need:str  ):

    wallet = get_one_wallet_by_uuid(user_id)  

    if wallet[0]["balance"] == 0:
        return

    print(religion, mood, need)



    put_value_in_wallet_by_user_id(wallet[0]["balance"]- 1, user_id) 
            
    message = integration_groq(prompt, religion, need, mood ) 

    return message
    







