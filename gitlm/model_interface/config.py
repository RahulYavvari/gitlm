import os

from gitlm.utils.config import _MODEL_FILENAME

from llama_cpp import Llama

llm = Llama(
    model_path=os.path.join(os.path.dirname(__file__), "../model", _MODEL_FILENAME),
    verbose=False,
    n_ctx=2048
)