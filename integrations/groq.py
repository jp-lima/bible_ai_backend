from dotenv import load_dotenv
import os
from groq import Groq
load_dotenv() 

API_KEY = os.getenv("GROQ_API_KEY")

def integration_groq(prompt,religion, need, mood, historic):


    lista = [
             {
        "role": "system",
        "content": f'''Você é um assistente espiritual.

                    Informações do usuário:
    - Afiliação religiosa: {religion}
    - Necessidade: {need}
    - Humor atual: {mood}

    Regras:
    1. Responda respeitando a afiliação religiosa.
    2. Ajude conforme a necessidade.
    3. Adapte o tom ao humor do usuário.
    4. Sempre finalize a resposta com uma conclusão completa, nunca pare no meio de uma frase.
    '''
    },  
          {
            "role": "user",
            "content": prompt
          }
        ]

    lista[1:1] = historic

    client = Groq(api_key=API_KEY)
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=lista,
        temperature=0.7,
        max_completion_tokens=350,
        top_p=1,
        stream=False,
        stop=None
    )

    return completion.choices[0].message.content

