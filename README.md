# dolphin3

`dolphin3` is a simple offline Python wrapper to query the **Dolphin 3** large language model via [Ollama](https://ollama.com/) and includes a convenient `%%dolphin3` **Jupyter cell magic** for interactive notebooks.

## 🚀 Features

- Offline access to the **Dolphin 3** LLM via Ollama
- Simple `ask_question()` function with input validation
- Jupyter notebook magic `%%dolphin3` for natural querying
- Easy to use and extend

## 📦 Installation

1. Clone or download this repository:

```bash
git clone https://github.com/DwaipayanDutta/dolphin3.git
cd dolphin3
```

2. Install in **editable** mode:

```bash
pip install -e .
```

> Make sure you have Python 3.7+ and `requests` installed.

## 🧠 Prerequisites

- Install [Ollama](https://ollama.com/download)
- Pull the Dolphin 3 model:

```bash
ollama pull dolphin3
```

- Run Ollama (usually auto-starts):

```bash
ollama run dolphin3
```

## 🧪 Usage in Python Scripts

```python
from dolphin3 import ask_question

response = ask_question("#What is the capital of France?")
print(response)
```

> Input must begin with a `#`, or you'll get an error.

## 📓 Usage in Jupyter Notebooks

### 1. Import the magic command:

```python
from dolphin3.magic import dolphin3
```

### 2. Use it in a cell:

```python
%%dolphin3
#Explain general relativity in simple terms.
```

Output appears directly below the cell!

## ⚙️ Configuration

Internally, the package sends a POST request to:

```
http://localhost:11434/api/generate
```

You can modify the temperature, stop sequences, or streaming behavior in `client.py` or `magic.py`.

## 📁 Project Structure

```
dolphin3/
├── dolphin3/
│   ├── __init__.py
│   ├── client.py       # Main logic
│   └── magic.py        # Jupyter cell magic
├── setup.py
├── requirements.txt
└── README.md
```

## 🛠️ Development

To edit and test in real time:

```bash
pip install -e .
```

## 🧾 License

MIT License

## 🤝 Contributions

PRs welcome! Please open an issue before submitting large changes.
