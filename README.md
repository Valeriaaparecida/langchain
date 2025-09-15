# 🤖 Projeto Multiagentes de IA com Gemini, LangChain e LangGraph  

Este repositório documenta **toda a trajetória de aprendizado** no processo de criação de **agentes de Inteligência Artificial**, culminando em um projeto de **multiagentes** que utiliza **Gemini (Google AI)** integrado com **LangChain** e **LangGraph**.  

## 🧠 Sobre o Projeto  
O objetivo é explorar como **agentes autônomos** podem ser criados, orquestrados e integrados em sistemas multiagentes, utilizando tecnologias modernas de LLMs e frameworks de coordenação.  

## 🔧 Tecnologias Utilizadas  
- [Gemini (Google AI)](https://ai.google.dev/) → modelo generativo usado como LLM principal  
- [LangChain](https://www.langchain.com/) → framework para criação de agentes e cadeias de raciocínio  
- [LangGraph](https://www.langchain.com/langgraph) → orquestração de fluxos multiagentes de forma gráfica e estruturada  
- [Python Dotenv](https://pypi.org/project/python-dotenv/) → gerenciamento seguro de variáveis de ambiente  

## 📂 Estrutura do Repositório  
- **/notebooks** → experimentos e estudos práticos com Gemini e agentes  
- **/src** → implementação dos agentes e fluxos multiagentes  
- **/docs** → anotações e referências teóricas do aprendizado  

## 🚀 Exemplo de Uso com Gemini  

```python
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv("API_KEY")

numero_dias = 5
numero_criancas = 2
atividade = "música"

prompt = f"Crie um roteiro de viagem de {numero_dias} dias, para uma família com {numero_criancas} crianças, que gosta de {atividade}"

# 1. Configure a API do Gemini
genai.configure(api_key=os.environ.get("API_KEY"))

# 2. Crie a instância do modelo
cliente = genai.GenerativeModel('gemini-2.5-flash')

# 3. Gere a resposta
response = cliente.generate_content(prompt)

# 4. Exiba a saída
print(response.text)
