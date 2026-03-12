from requests import Response
from fastapi import APIRouter, HTTPException, Request
from service.credits_service import obter_identificador_usuario, inicializar_creditos, usar_credito, CUSTO_POR_MENSAGEM
from service.gemini_service import processar_mensagem_gemini
from integrations.groq import integration_groq  
from service.chatbot_service import chatbot_message_service    
from models.chatbot_models import Request_send_message  

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)
@router.get("/teste")
async def teste():
    response = integration_groq()
    
    return response 


@router.post("/chat-api")
async def chat(request: Request_send_message):

    response = chatbot_message_service(request.user_id, request.prompt, request.religion, request.mood, request.need, request.historic )  

    return response  



@router.get("/creditos")
async def verificar_creditos(request: Request):
    """Retorna os créditos disponíveis do usuário"""
    print(request)
    user_id = obter_identificador_usuario(request)
    usuario = inicializar_creditos(user_id)
    
    return {
        "creditos": usuario['creditos'],
        "total_usado": usuario['creditos_usados']
    }
