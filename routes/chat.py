from fastapi import APIRouter, HTTPException, Request
from service.credits_service import obter_identificador_usuario, inicializar_creditos, usar_credito, CUSTO_POR_MENSAGEM
from service.gemini_service import processar_mensagem_gemini

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

@router.post("/chat-api")
async def chat(request: Request):
    dados = await request.json()
    
    user_id = obter_identificador_usuario(request)
    usuario = inicializar_creditos(user_id)
    
    if usuario['creditos'] < CUSTO_POR_MENSAGEM:
        raise HTTPException(status_code=403, detail={
            "erro": "Créditos esgotados",
            "mensagem": "Você atingiu o limite de mensagens gratuitas.",
            "creditos_restantes": usuario['creditos']
        })
    
    prompt = dados.get("msg")
    if not prompt:
        raise HTTPException(status_code=400, detail={"response": "Por favor, digite uma mensagem."})
    
    # ✅ USA CRÉDITO ANTES
    if not usar_credito(user_id):
        raise HTTPException(status_code=500, detail={"erro": "Erro ao descontar crédito"})
    
    resposta = processar_mensagem_gemini(
        prompt=prompt,
        historico_bruto=dados.get("chatHistory", []),
        religion=dados.get('religion', 'Cristianismo'),
        humor=dados.get('mood'),
        need=dados.get('needs'),
        modo=dados.get('mode')
    )
    
    return {"response": resposta}

@router.get("/creditos")
async def verificar_creditos(request: Request):
    """Retorna os créditos disponíveis do usuário"""
    user_id = obter_identificador_usuario(request)
    usuario = inicializar_creditos(user_id)
    
    return {
        "creditos": usuario['creditos'],
        "total_usado": usuario['creditos_usados']
    }