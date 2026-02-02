from fastapi import APIRouter,Form,File, UploadFile,Response, HTTPException
from repositories.user_repo import get_all_users,get_user_by_email
from service.user_service import verify_password, service_create_user,service_delete_user,service_get_all_users,service_update_password_user,service_update_users_infos     

from models.user import UserRequestLogin, UserCreateRequest, UserDeleteRequest,RequestGetAuthorization,RequestNewPassword,RequestPutUser       


router = APIRouter(
prefix="/users",
tags=["users"]
        )


# admin receber todos os usuários
@router.get("/")
def get_users(request:RequestGetAuthorization):
    #all_users = service_get_all_users(request.authorization)
    all_users = get_all_users()
    return all_users


@router.put("/")
def admin_put_user_infos(request: RequestPutUser):

    response = service_update_users_infos(request.authorization, request.user_id,request.password, request.user_name,request.phone,request.email)    

    return response


@router.put("/update-password")
def update_password(request:RequestNewPassword):


    response = service_update_password_user(request.authorization, request.new_password)


    return response 


@router.post("/auth")
def search_user(user:UserRequestLogin): 
    response_login = verify_password(user.email,user.password) 

    return response_login

@router.post("/user/delete")
def delete_user(user:UserDeleteRequest):

    response = service_delete_user(user.user_id, user.authorization)

    return response 

# Qualquer pessoa criar novo usuário
@router.post("/create-user")
def create(user:UserCreateRequest):

    response = service_create_user(user.email, user.password, user.name, user.phone )


    return response


