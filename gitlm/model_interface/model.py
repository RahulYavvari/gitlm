from gitlm.model_interface.config import llm

def model_inference(messages):
    stream_output = llm.create_chat_completion(
        messages=messages,
        max_tokens=512,
        stream=True
    )
    return stream_output