from models.webhook import Merchant, CustomerInfos, ShippingAdress
from repositories.user_repo import get_all_users
from service.analitycs_service import service_add_new_estatistic_on_analitycs, service_post_a_user_online
from repositories.subscription_repo import *
from repositories.wallet_repo import *  
from repositories.plans_repo import get_plan_by_id   




def receive_payment_from_webhook(data):


    if data["event"] == "PAYMENT_RECEIVED": 

        put_subscription_by_payment_id(data["payment"]["subscription"], "live")

        subscription = get_subscription_by_payment_id(data["payment"]["subscription"])

        plan = get_plan_by_id(subscription["plan_id"])

        print(plan)

        print(subscription)

        put_value_in_wallet_by_user_id(plan[0]["credits_per_circle"], subscription["user_id"])   






