from os import access, confstr
from fastapi.responses import JSONResponse
from repositories.user_repo import del_user, get_all_users,get_user_by_email, post_new_user, get_user_by_id, put_user    
from utils import access_token
from utils.password import create_hash, verify_hash
from utils.access_token import create_access_token, decode_access_token
from service.analitycs_service import service_add_new_estatistic_on_analitycs, service_post_a_user_online 
import uuid
from datetime import datetime



def verify_password(email:str, password:str):
    user =  get_user_by_email(email)
    
    if not user:

        return JSONResponse(
                    status_code=404,
                    content="Email não encontrado no banco de dados"

                )
    
    elif verify_hash(password, user["password_hash"]):
        
        token = create_access_token(user["id"],user["name"],user["role"])

        return JSONResponse(
                status_code=201,
                content={"username":user["name"],"role":user["role"],"user_id": user["id"], "phone":user["phone"], "access_token":token, }
                )
    else:
        return JSONResponse(
                status_code=401,
                content="Não autorizado"
                )

def service_update_users_infos(authorization:str, user_id:str, password:str, username:str,phone:str, email:str):
    hashed_password = None
    user = get_user_by_id(user_id)
    if password:

        hashed_password = create_hash(password)
    
    decoded_token = decode_access_token(authorization)
    if decoded_token["role"] == "admin" or decoded_token["sub"] == user_id:
        print("autorizado")

        infos_user = {"user_id":user_id, "name":username, "email":email, "password_hash":hashed_password, "phone":phone }

        for key, value in infos_user.items():
            if not value:
                infos_user[key] = user[0][key]
   
        put_user(infos_user["name"], infos_user["phone"], infos_user["email"], infos_user["password_hash"], infos_user["user_id"])

    else:
        return JSONResponse(status_code=401,
                            content="Unauthorized")

    return decoded_token


def service_update_password_user(authorization:str, new_password:str):
    
       return JSONResponse(
            status_code=200,
            content= "senha alterada com sucesso"
            )

def service_get_all_users(authorization:str):

    access = decode_access_token(authorization)
    
    if(access["role"] == "admin"):

        all_users = get_all_users()

        return all_users
    else:
        return "não autorizado"

def service_create_user(email:str, password:str, name:str, phone:str):
    
    hashed_password = create_hash(password)
    new_uuid = uuid.uuid4()

    now = datetime.now()

    formato_iso = now.strftime("%Y-%m-%d %H:%M:%S.%f")

    post_new_user(str(new_uuid), name,email, hashed_password, formato_iso, phone)
   
    service_post_a_user_online("new_user", "user")
    service_add_new_estatistic_on_analitycs({"estatistic":"new_user", "data":""})

    return "user criado"



def service_delete_user(uuid:str, authorization:str):

    decoded_token = decode_access_token(authorization)

    if decoded_token["role"] == "admin":
           
        del_user(str(uuid))

        return "concluido"
        

    else:
        return "não autorizado"

 





