from openai import OpenAI
import ollama
import streamlit as st


with st.sidebar:
    model_list = ollama.list()  
    models = model_list.models 
    list_models = []
    for model in models:
        list_models.append(model.model)
    
    models_option = st.selectbox(
        "Ollama Model",
        list_models,
        index=None,
        placeholder="Select a model",
    )
    
    "[Download Ollama](https://ollama.com/download)"
    "[View the source code](https://github.com/sky150/Ollama-chatbot/Chatbot.py)"

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Ollama")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not models_option:
        st.info("Please add an ollama model to continue.")
        st.stop()
        
    client = ollama
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat(model=models_option, messages=st.session_state.messages)
    msg = response["message"]["content"].strip()
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    
    