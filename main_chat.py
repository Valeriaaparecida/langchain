import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

modelo = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)

lista_perguntas = [
    "Quero visitar um lugar no Brasil, famosos por praias e cultura. Pode sufgerir?",
    "Qual a melhor época do ano para ir?"
]

for uma_pergunta in lista_perguntas:
    resposta = modelo.invoke(uma_pergunta)
    print("Usuario: ", uma_pergunta),
    print("IA: ", resposta.content, "\n")