import whisper
import sys
import time
from functools import wraps
import mlx_whisper


import warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")


model = whisper.load_model("large")
model.eval()


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to complete.")
        return result
    return wrapper




@measure_time
def audio_to_text(audio_file):
    print("-------------------------------------") 
    print(" Running audio_to_text function") 
    print("-------------------------------------")
    result = model.transcribe(audio_file)
    print("The result is:"+result["text"])
    

@measure_time
def audio_to_text_mlx(audio_file):
    print("-------------------------------------")
    print(" Running audio_to_text_mlx function") 
    print("-------------------------------------")
    result = mlx_whisper.transcribe(audio_file, path_or_hf_repo="mlx-community/whisper-large-v3-mlx")
    #text = mlx_whisper.transcribe(audio_file)["text"]
    print("The result is:"+result["text"])



def main(audio_file):
    audio_to_text_mlx(audio_file)
    audio_to_text(audio_file)
    #audio_to_text_coreml(audio_file)
   

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python whisper_poc.py <audio_file>")
    else:
        audio_file = sys.argv[1]
        main(audio_file)
