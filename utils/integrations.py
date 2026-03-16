from dotenv import load_dotenv
import requests
import os

load_dotenv()

asaas_acess_token = os.getenv("API_KEY_ASAAS")
asaas_base_url = os.getenv("BASE_URL_ASAAS")
asaas_api = f'{asaas_base_url}/v3/customers'  

def create_new_client(user_name:str, user_cpf:str):
    print(asaas_api, "AQUI")

    payload = {
            "name":user_name,
            "cpfCnpj":user_cpf
        }

    headers = {
        "accept":"application/json",
        "content-type": "application/json",
    "access_token":asaas_acess_token  
        }

    response = requests.post(asaas_api, headers=headers, json=payload)

    return response

def get_checkout(subscription_id):

    #url = "https://sandbox.asaas.com/api/v3/payments"
    
    url = f'{asaas_base_url}/v3/payments'

    headers = {
        "access_token": asaas_acess_token  
    }

    params = {
        "subscription": subscription_id  
    }

    response = requests.get(url, headers=headers, params=params)

    return response.json()










