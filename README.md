

# 🚀 Projeto Multiagentes de IA  

Este repositório documenta **toda a trajetória de aprendizado** no processo de criação de **agentes de Inteligência Artificial**, desde os conceitos iniciais até a implementação prática de arquiteturas multiagentes.  

## 🧠 Sobre o Projeto  
O objetivo deste projeto é explorar e consolidar o aprendizado no desenvolvimento de **agentes autônomos de IA**, com foco em:  
- Criação e orquestração de agentes inteligentes  
- Comunicação e colaboração entre múltiplos agentes  
- Aplicação de técnicas modernas para fluxos de decisão e raciocínio  

## 🔧 Tecnologias Utilizadas  
- [LangChain](https://www.langchain.com/) → framework para construção de agentes e cadeias de raciocínio  
- [LangGraph](https://www.langchain.com/langgraph) → para orquestração de fluxos multiagentes de forma gráfica e estruturada  


# LangChain e Python: criando ferramentas com a LLM OpenAI

## ⚙️ Guia de Configuração

Siga os passos abaixo para configurar seu ambiente e utilizar os scripts do projeto.

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
```

