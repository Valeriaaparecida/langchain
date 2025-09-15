from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


numero_dias = 5
numero_criancas = 2
atividade = "praia"

prompt = f"Crie um roteiro de viagens, para um período de {numero_dias} dias, para uma família com {numero_criancas} crianças, com foco em atividades de {atividade}."

modelo = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)

resposta = modelo.invoke(prompt)
print(resposta.content)