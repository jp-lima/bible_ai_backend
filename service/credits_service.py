from fastapi import Request

# Armazenamento em memória
creditos_users = {}
CREDITOS_INICIAIS = 5
CUSTO_POR_MENSAGEM = 1

def obter_identificador_usuario(request: Request):
    ip = request.client.host
    user_agent = request.headers.get('user-agent', '')
    return f"{ip}_{hash(user_agent)}"

def inicializar_creditos(user_id: str):
    if user_id not in creditos_users:
        creditos_users[user_id] = {
            'creditos': CREDITOS_INICIAIS,
            'creditos_usados': 0
        }
    return creditos_users[user_id]

def usar_credito(user_id: str):
    usuario = creditos_users.get(user_id)
    if usuario and usuario['creditos'] >= CUSTO_POR_MENSAGEM:
        usuario['creditos'] -= CUSTO_POR_MENSAGEM
        usuario['creditos_usados'] += CUSTO_POR_MENSAGEM
        return True
    return False

def verificar_creditos_disponiveis(user_id: str):
    usuario = creditos_users.get(user_id)
    return usuario and usuario['creditos'] >= CUSTO_POR_MENSAGEM