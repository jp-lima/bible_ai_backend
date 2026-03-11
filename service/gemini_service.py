import requests
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()



CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY").strip()
MODELO_ESCOLHIDO = "gemini-2.5-flash-lite"
BASE_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELO_ESCOLHIDO}:generateContent?key={CHAVE_API_GOOGLE}"
print(f"🔑 CHAVE_API_GOOGLE: {CHAVE_API_GOOGLE}")
def processar_mensagem_gemini(prompt, historico_bruto, religion, humor, need, modo):
    """Processa mensagem através do Gemini API"""
    
    historico_conversa = []
    for mensagem in historico_bruto:
        papel = "user" if mensagem["sender"] == "sender" else "model"
        historico_conversa.append({"role": papel, "parts": mensagem["text"]})
    
    maximo_tentativas = 1
    repeticao = 0

    while True:
        try:
            prompt_do_sistema = f"""
Você é uma Assistente Espiritual Pessoal, dedicada a acompanhar o usuário em sua jornada dentro da religião {religion}.

Seu objetivo é tirar dúvidas, explicar ensinamentos, textos e princípios espirituais, além de oferecer orientação e conforto de acordo com a tradição de fé escolhida.

CONTEXTO ATUAL:
- Religião do usuário: {religion}
- Humor do usuário: {humor}
- Necessidade do usuário: {need}
- Modo de interação: {modo}

DIRETRIZES DE ASSISTÊNCIA:

1. REGRA DE OURO (RELIGIÃO):
Responda ESTRITAMENTE com base nos ensinamentos, textos e princípios da religião {religion}.  
Nunca misture religiões ou compare crenças diferentes.

2. IDENTIDADE RELIGIOSA:
- Se a religião for Cristianismo, utilize a Bíblia e cite versículos (ex: Filipenses 4:13).
- Se a religião for Budismo, utilize os ensinamentos do Buda, como as Quatro Nobres Verdades, o Caminho Óctuplo e os Sutras.
Use sempre a linguagem e os conceitos próprios da religião {religion}.

3. INTERATIVIDADE:
Explique com clareza e, ao final, faça uma pergunta que incentive reflexão ou aprofundamento dentro da fé do usuário.

4. FOCO EM DÚVIDAS ESPIRITUAIS:
Se o usuário enviar apenas um texto sagrado ou conceito, pergunte se ele deseja uma explicação do significado, do contexto ou uma reflexão prática para a vida.

5. SEGURANÇA E COERÊNCIA:
Nunca mencione, discuta ou explique outras religiões além da religião {religion}.

6. FILTRO DE TEMA:
Responda APENAS perguntas relacionadas à espiritualidade, ensinamentos, textos sagrados e vida de fé da religião {religion}.  
Caso o tema seja outro, responda:
"Como sua assistente espiritual, meu propósito é ajudar você dentro da fé {religion}. Posso te ajudar com algum ensinamento hoje?"

7. CONTEÚDO SENSÍVEL:
Se detectar intenção de violência, automutilação ou dano, recuse de forma acolhedora e oriente a buscar ajuda espiritual ou profissional, mantendo a linguagem da religião {religion}.

8. EMOÇÕES HUMANAS:
Se o usuário expressar sentimentos, responda com ensinamentos da religião {religion} que tragam conforto e clareza. Não bloqueie emoções naturais.
"""

            # Preparar o conteúdo da requisição
            contents = []
            
            # Adicionar o histórico de conversa
            for mensagem in historico_conversa:
                contents.append({
                    "role": mensagem["role"],
                    "parts": [{"text": mensagem["parts"]}]
                })
            
            # Adicionar a mensagem atual do usuário
            contents.append({
                "role": "user",
                "parts": [{"text": prompt}]
            })
            
            # Payload da requisição
            payload = {
                "contents": contents,
                "systemInstruction": {
                    "parts": [{"text": prompt_do_sistema}]
                },
                "generationConfig": {
                    "temperature": 0.1,
                    "maxOutputTokens": 8192
                },
                "safetySettings": [
                    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_LOW_AND_ABOVE"},
                    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"},
                    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_LOW_AND_ABOVE"},
                    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"}
                ]
            }
            
            # Fazer a requisição HTTP
            response = requests.post(
                BASE_URL,
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            
            # Verificar se a requisição foi bem-sucedida
            if response.status_code == 200:
                resultado = response.json()
                texto_resposta = resultado["candidates"][0]["content"]["parts"][0]["text"]
                return texto_resposta
            else:
                raise Exception(f"Erro na API: {response.status_code} - {response.text}")
            
        except Exception as erro:
            if "safety" in str(erro).lower() or "blocked" in str(erro).lower():
                return f"Como sua assistente espiritual em {religion}, busco manter nossa conversa focada em princípios de paz. Como posso te ajudar hoje? 🙏"
            
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return f"Erro no Gemini: {erro}"
            
            sleep(2)
