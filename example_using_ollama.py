import ollama

# Inicializa o Ollama client, mesma coisa que dar um ollama serve no terminal
client = ollama.Client()

# Definir o modelo de IA e o prompt
model = "llama2"
prompt = "What is Python?"

# Recebe a resposta do client
response = client.generate(model=model, prompt=prompt)

# Printa os resultados
print("Response from Ollama:")
print(response.response)