import os
from dotenv import load_dotenv 
from repositories.plans_repo import get_plan_by_id 
from repositories.subscription_repo import *
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from datetime import datetime, time, timedelta
import uuid
import requests
from utils.integrations import *  
from service.user_service import *
from repositories.user_repo import * 
from repositories.user_repo import get_all_users
from repositories.plans_repo import get_all_plans 

load_dotenv()

asaas_acess_token = os.getenv("API_KEY_ASAAS")

asaas_base_url = os.getenv("BASE_URL_ASAAS")
asaas_api = f'{asaas_base_url}/v3/subscriptions'


def service_get_all_subscriptions(authorization:str):
# 1. Busca os dados das três fontes
    subs = get_all_subscriptions()
    plans = get_all_plans()
    users = get_all_users()

    # 2. Cria mapas de busca para acesso instantâneo O(1)
    plan_map = {p['id']: p['name'] for p in plans}
    
    # Criamos um mapa que guarda um dicionário com nome e email para cada ID de usuário
    user_map = {u['id']: {'name': u['name'], 'email': u.get('email')} for u in users}

    # 3. Constrói a lista final enriquecida
    enriched_subscriptions = []
    
    for sub in subs:
        item = sub.copy()
        
        p_id = sub.get('plan_id')
        u_id = sub.get('user_id')
        
        # Adiciona o nome do plano
        item['plan_name'] = plan_map.get(p_id, "Plano não encontrado")
        
        # Busca os dados do usuário no mapa
        user_info = user_map.get(u_id)
        
        if user_info:
            item['user_name'] = user_info['name']
            item['user_email'] = user_info['email']
        else:
            item['user_name'] = "Usuário não encontrado"
            item['user_email'] = None
        
        enriched_subscriptions.append(item)

    return enriched_subscriptions

def service_create_subscription(user_id, plan_id, user_cpf, billing_type, user_name, cycle):
    now = datetime.now(ZoneInfo("America/Sao_Paulo"))
    new_uuid = uuid.uuid4()

    plan = get_plan_by_id(plan_id)
    plan_table = {
            "monthly":{"value":plan[0]["price_monthly"], "days_quantity":30},
            "quarterly":{"value":plan[0]["price_quartely"], "days_quantity":90},
            "semiannually":{"value":plan[0]["price_semiannual"], "days_quantity":180}
                           
        }

    new_client = create_new_client(user_name, user_cpf)
    data_new_client = new_client.json()

    put_asaas_user_id(user_id, data_new_client["id"] )
    

    next_payment = now + timedelta(days=plan_table[cycle]["days_quantity"])



    payload = {
        "customer":data_new_client["id"],    
        "billingType":billing_type,
        "value":plan_table[cycle]["value"],
        "nextDueDate":next_payment.strftime("%Y-%m-%d"),
        "cycle":cycle.upper(), #<- O asass só aceita o "cycle" em letra maiusculas
    }
    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "access_token": asaas_acess_token
    }
    response = requests.post(asaas_api, json=payload, headers=headers)

    data = response.json()
    print(data)
    
    create_row_subscription(str(new_uuid),user_id,plan_id,"waiting_payment" ,next_payment, data["id"], now   )

    checkout = get_checkout(data["id"])
    print(checkout)

    return checkout["data"][0]["invoiceUrl"]










