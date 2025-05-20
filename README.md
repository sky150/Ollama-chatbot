# 🎈 Ollama Chatbot  
*A local AI chatbot powered by Ollama – lightweight, private, and offline-ready*

![Demo](demo.gif) *(Optional: Add a screenshot/GIF later)*  

---

## 🌟 **Features**  
✅ **Local & Private** – No cloud API calls, runs entirely on your machine  
✅ **Any Ollama Model** – Use `llama3`, `mistral`, or custom models  
✅ **Simple UI** – Built with Streamlit (no complex setup)  

---

## 🛠️ **Installation**  

### 1. **Install Ollama**  
Download and run the Ollama server:  
🔗 [https://ollama.ai/download](https://ollama.ai/download)  

### 2. **Download a Model**  
Example:  
```bash
ollama pull llama3
```

### 3. **Clone repository**
```bash
git clone ...
```

### 4. Run locally
```bash
pyenv virtualenv 3.10.6 llm-examples
pyenv activate llm-examples
make install
make run
```

