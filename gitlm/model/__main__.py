import os
from gitlm.utils.config import _MODEL_URL
from gitlm.model.download_model import download_file_from_url

if __name__ == "__main__":
    MODEL_URL = _MODEL_URL

    model_filename = MODEL_URL.split("/")[-1]
    
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    
    output_file_path = os.path.join(current_script_dir, model_filename)

    print("Attempting to download the TinyLlama GGUF model...")
    download_file_from_url(MODEL_URL, output_file_path)