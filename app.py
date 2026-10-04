import streamlit as st
import requests

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Assistant")
st.write("Ask questions and get answers from AI.")

mode = st.selectbox(
    "Choose a mode",
    ["Ask Question", "Explain Topic", "Give Example"]
)

question = st.chat_input("Type your question...")

if question:

    if mode == "Ask Question":
        prompt = question

    elif mode == "Explain Topic":
        prompt = f"Explain {question} in simple English."

    else:
        prompt = f"Give a simple example for {question}."

    with st.chat_message("user"):
        st.write(question)

    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama3.2",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "stream": False
            },
            timeout=120
        )

        data = response.json()
        answer = data["message"]["content"]

        with st.chat_message("assistant"):
            st.write(answer)

    except:
        st.error("AI is not connected. Please start Ollama.")