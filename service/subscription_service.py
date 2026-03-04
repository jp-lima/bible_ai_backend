import os
from dotenv import load_dotenv
from repositories.plans_repo import get_plan_by_id
from repositories.subscription_repo import *
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from datetime import datetime, time, timedelta
import uuid
import requests
from utils.integrations import create_new_client 
from service.user_service import *
from repositories.user_repo import * 

load_dotenv()

asaas_acess_token = os.getenv("API_KEY_ASAAS")

asaas_api = "https://api-sandbox.asaas.com/v3/subscriptions"


def service_create_subscription(user_id, plan_id, user_cpf, billing_type, user_name, cycle):
    now = datetime.now(ZoneInfo("America/Sao_Paulo"))
    new_uuid = uuid.uuid4()

    plan = get_plan_by_id(plan_id)
    print(plan)
    print(plan[0]["name"])
    plan_price_table = {
            "monthly":plan[0]["price_monthly"],
            "quartely":plan[0]["price_quartely"],
            "semiannualy":plan[0]["price_semiannual"]
        }


    new_client = create_new_client(user_name, user_cpf)
    data_new_client = new_client.json()

    put_asaas_user_id(user_id, data_new_client["id"] )
    

    next_payment = now + timedelta(days=30)


    print(next_payment.strftime("%Y-%m-%d"))

    print(plan_price_table[cycle])
 #   create_row_subscription(str(new_uuid),user_id,plan_id,"waiting_payment" ,next_payment, "", now   )
    payload = {
        "customer":data_new_client["id"],    
        "billingType":billing_type,
        "value":plan_price_table[cycle],
        "nextDueDate":next_payment.strftime("%Y-%m-%d"),
        "cycle":cycle.upper(), #<- O asass só aceita o "cycle" em letra maiusculas
    }
    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "access_token": asaas_acess_token
    }
    response = requests.post(asaas_api, json=payload, headers=headers)

    print(response.text)
    
    # Colocar id do pagamento response["id"] na coluna payment_provider_id da tabela subscriptions
    # colocar os creditos na carteira do cliente
    # Atualizar o subscription de "waiting_payment" para "paid"






