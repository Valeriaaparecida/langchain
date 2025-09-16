# 🤖 Projeto Multiagentes de IA com Gemini, LangChain e LangGraph  

Este repositório documenta **toda a trajetória de aprendizado** no processo de criação de **agentes de Inteligência Artificial**, culminando em um projeto de **multiagentes** que utiliza **Gemini (Google AI)** integrado com **LangChain** e **LangGraph**.  

## 🧠 Sobre o Projeto  
O objetivo é explorar como **agentes autônomos** podem ser criados, orquestrados e integrados em sistemas multiagentes, utilizando tecnologias modernas de LLMs e frameworks de coordenação.  

## 🔧 Tecnologias Utilizadas  
- [Gemini (Google AI)](https://ai.google.dev/) → modelo generativo usado como LLM principal  
- [LangChain](https://www.langchain.com/) → framework para criação de agentes e cadeias de raciocínio  
- [LangGraph](https://www.langchain.com/langgraph) → orquestração de fluxos multiagentes de forma gráfica e estruturada  
- [Python Dotenv](https://pypi.org/project/python-dotenv/) → gerenciamento seguro de variáveis de ambiente  

## ⚙️ Guia de Configuração

O script abaixo é para usar com chave da OpenAI e serve de base para os primeiros passos apesar de que esse projeto foir feito com llm do Gemini

### 1. Criar e Ativar Ambiente Virtual

**Windows:**
```bash
python -m venv langchain
langchain\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv langchain
source langchain/bin/activate
```

### 2. Instalar Dependências

Utilize o comando abaixo para instalar as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 3. Configurar Chave da OpenAI

Crie ou edite o arquivo `.env` adicionando sua chave de API da OpenAI:
```bash
OPENAI_API_KEY="SUA_CHAVE_DE_API"
```o  



# 3. Gere a resposta
response = cliente.generate_content(prompt)

# 4. Exiba a saída
print(response.text)


