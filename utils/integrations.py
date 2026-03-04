from dotenv import load_dotenv
import requests

asaas_api = "https://api-sandbox.asaas.com/v3/customers"


def create_new_client(user_name:str, user_cpf:str):

    payload = {
            "name":user_name,
            "cpfCnpj":user_cpf
        }

    headers = {
        "accept":"application/json",
        "content-type": "application/json",
    "access_token": "$aact_hmlg_000MzkwODA2MWY2OGM3MWRlMDU2NWM3MzJlNzZmNGZhZGY6OmE2MTllZGFkLTQ4YTktNDRiOS05NWJkLTQ5NTYxM2ZlOGJhMDo6JGFhY2hfZjc5N2RhNTUtMzIxMC00ZGRhLWJiYzUtOTk3YjJlZTE4OTNl"
        }

    response = requests.post(asaas_api, headers=headers, json=payload)

    return response










