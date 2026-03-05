from models.webhook import Merchant, CustomerInfos, ShippingAdress
from repositories.user_repo import get_all_users
from service.analitycs_service import service_add_new_estatistic_on_analitycs, service_post_a_user_online
from repositories.subscription_repo import *




def receive_payment_from_webhook(data):
    


    if data["event"] == "PAYMENT_RECEIVED": 

        put_subscription_by_payment_id(data["payment"]["subscription"], "live")





