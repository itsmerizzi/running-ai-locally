# 🤖 Project: Using Ollama with Python – Example

This project demonstrates how to use locally hosted AI models with [Ollama](https://ollama.com/), integrating them into Python via two methods: using the official `ollama` Python library and through direct HTTP requests using `requests`.

---

## 📦 Requirements

Before starting, make sure you have the following installed:

- Python 3.7 or higher
- `pip` (Python package manager)
- [Ollama](https://ollama.com/)

---

## 🧠 Installing Ollama and Downloading a Model

1. **Install Ollama:**  
   Go to [https://ollama.com/download](https://ollama.com/download) and follow the installation instructions for your operating system.

2. **Download an AI model (e.g., Llama2):**

   Run the following in your terminal:
   ```bash
   ollama run llama2
   ```
   Or:
   ```bash
   ollama pull llama2
   ```

3. **Start the local Ollama service:**
   ```bash
   ollama serve
   ```
   This will start a local server that can receive HTTP API calls.

---

## 🔧 Setting Up the Python Environment

1. Clone this repository or download the project files.

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📁 Project Structure

```text
├── example_using_ollama.py      # Uses the official Ollama Python client
├── example_using_requests.py    # Uses raw HTTP requests to interact with the API
├── requirements.txt             # Lists the required dependencies
```

---

## ▶️ How to Use

### 1. Using `example_using_ollama.py`:

This script uses the `ollama` Python client to interact with the model.

```bash
python example_using_ollama.py
```

Example output:
```
Response from Ollama:
Python is a high-level, interpreted programming language...
```

---

### 2. Using `example_using_requests.py`:

This script makes a direct POST request to the local Ollama API and streams the response.

```bash
python example_using_requests.py
```

Example output:
```
Streaming response from Ollama:
Python is a powerful and easy-to-learn language...
```

---

## 🧪 Dependencies

Listed in the `requirements.txt` file:

```
requests
ollama
```

Install them using:
```bash
pip install -r requirements.txt
```

---

## 📌 Notes

- The default model used is `llama2`, but you can change it to any other model available on [ollama.com](https://ollama.com/library), as long as it's downloaded.
- Make sure the Ollama server is running (`ollama serve`) before using the `example_using_requests.py` script.

---

## 🧠 About Ollama

Ollama allows you to run large language models (LLMs) locally with ease. It's a great solution for developers and enthusiasts who want to explore AI without relying on cloud services.

---

## 📃 License

This is an educational/demo project and does not have a specific license.
