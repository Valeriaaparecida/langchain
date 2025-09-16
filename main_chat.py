import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory



load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

modelo = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)

prompt_sugestao = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um guia de viagem especializado em destinos brasileiros. Apresente-se como Sr. Magnum "),
        ("placeholder", "{historico}"),
        ("human", "{query}")
    ]
)

cadeia =prompt_sugestao | modelo | StrOutputParser()

memoria = {}
sessao = "aula_langchain"

def historico_por_sessao(sessao : str):
    if sessao not in memoria:
        memoria[sessao] = InMemoryChatMessageHistory()
    return memoria[sessao]    

lista_perguntas = [
    "Quero visitar um lugar no Brasil, famosos por praias e cultura. Pode sufgerir?",
    "Qual a melhor época do ano para ir?"
]

cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=cadeia,
    get_session_history=historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico"
)

for uma_pergunta in lista_perguntas:
    resposta =cadeia_com_memoria.invoke(
        {
            "query" : uma_pergunta
        },
        config={"session_id": sessao}
    )
    print("Usuario: ", uma_pergunta),
    print("IA: ", resposta, "\n")