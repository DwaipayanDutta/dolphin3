import requests

def ask_question(question: str) -> str:
    """
    Accept a question starting with '#' and return an answer from Dolphin 3 via Ollama.
    """
    question = question.strip()
    if not question.startswith("#"):
        return "Error: Question must start with '#' symbol."

    clean_question = question[1:].strip()

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "dolphin3",
                "prompt": clean_question,
                "stream": False,
                "stop": ["</s>", "###", "User:"],
                "temperature": 0.0,
                "max_tokens": 256
            }
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()

    except requests.exceptions.RequestException as e:
        return f"Error connecting to Dolphin 3 via Ollama: {str(e)}"
