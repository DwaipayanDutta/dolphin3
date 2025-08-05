from .client import ask_question

# Auto-register magic if in IPython
try:
    from IPython import get_ipython
    if get_ipython():
        from . import magic
except ImportError:
    pass

__all__ = ["ask_question"]
