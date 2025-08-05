import streamlit as st
import requests

st.set_page_config(page_title="Dolphin 3 Chat", layout="centered")

st.title("🤖 Dolphin 3 - Offline LLM (via Ollama)")
st.markdown("Ask a question (must start with `#`) and get a response from the Dolphin 3 model running locally via Ollama.")

question = st.text_area("Your Question", placeholder="#What is the capital of Japan?")

if st.button("Ask Dolphin 3"):
    if not question.strip().startswith("#"):
        st.error("Your question must start with '#'")
    else:
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "dolphin3",
                    "prompt": question.strip()[1:].strip(),
                    "stream": False,
                    "stop": ["</s>", "###", "User:"],
                    "temperature": 0.0,
                    "max_tokens": 256
                }
            )
            response.raise_for_status()
            data = response.json()
            st.success(data.get("response", "").strip())
        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}")
