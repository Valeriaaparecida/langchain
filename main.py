import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

numero_dias = 5
numero_criancas = 2
atividade = "música"

prompt = f"Crie um roteiro de viagem de {numero_dias} dias, para uma familia com {numero_criancas} crianças, que gosta de {atividade}"

# 1. Configure a API do Gemini
genai.configure(api_key=os.environ.get("API_KEY"))

# 2. Crie a instância do modelo
cliente = genai.GenerativeModel('gemini-2.5-flash')

# 3. Use o método generate_content() para obter a resposta
response = cliente.generate_content(prompt)

# 4. Imprima o texto da resposta
print(response.text)