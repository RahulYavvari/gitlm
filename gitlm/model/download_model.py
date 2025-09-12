import os
import requests
from tqdm import tqdm

def download_file_from_url(url: str, output_path: str):
    if os.path.exists(output_path):
        print(f"File already exists at '{output_path}'. Skipping download.")
        return

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get("Content-Length", 0))
        
        with open(output_path, "wb") as file, tqdm(
            desc=os.path.basename(output_path),
            total=total_size,
            unit="iB",
            unit_scale=True,
            unit_divisor=1024,
        ) as progress_bar:
            for chunk in response.iter_content(chunk_size=8192):
                progress_bar.update(len(chunk))
                file.write(chunk)

        print(f"\nDownload complete. File saved to: '{output_path}'")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        if os.path.exists(output_path):
            os.remove(output_path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        if os.path.exists(output_path):
            os.remove(output_path)