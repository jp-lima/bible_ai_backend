from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv() 

API_KEY = os.getenv("GROQ_API_KEY ")

def integration_groq(prompt,religion, need, mood):
    client = Groq(api_key=API_KEY)
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
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
    3. Adapte o tom ao humor do usuário.'''
},
          {
            "role": "user",
            "content": prompt
          }
        ],
        temperature=1,
        max_completion_tokens=200,
        top_p=1,
        stream=False,
        stop=None
    )

    return completion.choices[0].message.content

