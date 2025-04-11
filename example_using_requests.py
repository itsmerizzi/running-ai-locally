import requests
import json

# URL para chamar a API do Ollama
url = "http://127.0.0.1:11434/api/chat"

payload = {
    "model": "llama2",
    "messages": [{"role": "user", "content": "What is Python?"}] # Aqui poderia ser um input para o usuário, mas é só um exemplo
}

# Manda um POST com stream ativado, esse stream mantem a conexão rodando
response = requests.post(url=url, json=payload, stream=True)

# Valida o status
if response.status_code == 200:
    print("Streaming response from Ollama:")
    for line in response.iter_lines(decode_unicode=True):
        if line: # Ignora linhas vazias
            try:
                # Parse na linha
                json_data = json.loads(line)
                # Printa somente a mensagem do assistente de IA
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"], end="")
            except json.JSONDecodeError:
                print(f"\nError decoding line: {line}")