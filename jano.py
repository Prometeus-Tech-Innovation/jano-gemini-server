import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ['API_KEY'])
model = genai.GenerativeModel("tunedModels/jano-v2-vzxrel0vrro8")

chat = model.start_chat(history=[
    {"role": "user", "parts": "Responda com no máximo 300 caracteres como um personagem histórico envolvido no tópico da pergunta, ou aja como alguém que fez parte do tópico."}
])


def make_question(question: str):
    res = chat.send_message(question)
    return res.text
