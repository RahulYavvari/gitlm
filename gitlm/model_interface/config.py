import os
import sys

from utils.config import _MODEL_FILENAME

from llama_cpp import Llama
from config import _MODEL_FILENAME

llm = Llama(
    model_path="model/" + _MODEL_FILENAME,
    verbose=False, 
    n_ctx=2048
)
