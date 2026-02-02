from fastapi import APIRouter
from repositories.analitycs_repo import create_row_of_analitycs, get_rows_of_analitycs, put_row_of_analityc   
from service.analitycs_service import service_add_new_estatistic_on_analitycs, service_post_a_user_online
from repositories.analitycs_users_activity import get_all_rows_from_analitycs_users, create_row_analitycs_users
from models.analitycs import getAuthorization 

router = APIRouter(

prefix = "/analitycs",
tags=["analitycs"]


)

# Criar usuário, compra paga, valor da compra


@router.get("/")
def send_analitycs_by_mounth():

    response = get_rows_of_analitycs()

    return response

@router.get("/users-activity")
def send_analitycs_of_users_activity():

    response = get_all_rows_from_analitycs_users()
    return response



@router.post("/user-loged")
def user_be_loged(request:getAuthorization):


#    teste = get_all_rows_from_analitycs_users()
    service_add_new_estatistic_on_analitycs({"estatistic":"users_online", "data":500.8})
 #   create_row_analitycs_users("2026-01-16 15:01:51.122725", 0, 0)

    return  
@router.get("/teste")
def test():
    
    service_add_new_estatistic_on_analitycs({"estatistic":"users_online", "data":500.8})



