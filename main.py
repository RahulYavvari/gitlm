from llama_cpp import Llama
from config import _MODEL_FILENAME

llm = Llama(
    model_path="model/" + _MODEL_FILENAME,
    verbose=False, 
    n_ctx=2048
)

messages = [
    {
        "role": "user",
        "content": "Give command for git diff for everything in the repo",
    }
]

stream_output = llm.create_chat_completion(
    messages=messages,
    max_tokens=512,
    stream=True
)

for chunk in stream_output:
    delta = chunk["choices"][0]["delta"]
    if "content" in delta:
        print(delta["content"], end="", flush=True)

# print(output["choices"][0]["message"]["content"]) # stream=False