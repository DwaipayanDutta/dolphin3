from IPython.core.magic import register_cell_magic
import requests

@register_cell_magic
def dolphin3(line, cell):
    """
    Jupyter cell magic to query Dolphin 3 via Ollama.
    Usage:
    %%dolphin3
    #Your question here
    """
    question = cell.strip()

    if not question.startswith("#"):
        print("Error: Question must start with '#' symbol.")
        return

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
        print(data.get("response", "").strip())

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
