from fastapi import FastAPI, UploadFile, File, Form,Response 


from repositories.user_repo import get_all_users,get_user_by_email
from routes import analitycs
from service.user_service import verify_password, service_create_user, service_delete_user
from models.user import UserRequestLogin, UserCreateRequest, UserDeleteRequest    

from fastapi.middleware.cors import CORSMiddleware
from routes.users import router as users_router
from routes.webhook import router as webhook_yampi
from routes.analitycs import router as analitycs_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analitycs_router)
app.include_router(webhook_yampi)
app.include_router(users_router)
