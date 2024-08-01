import whisper
import mlx_whisper
import sys
import warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

model = whisper.load_model("large")
model.eval()

def convert_audio_to_text(audio_file):
  print("in convert audio to text")
  print(audio_file)
  try:
    print("Audio file type:", type(audio_file))
    audio_data = audio_file.read()
    #result = mlx_whisper.transcribe(audio_data, path_or_hf_repo="mlx-community/whisper-large-v3-mlx")
    result = mlx_whisper.transcribe("./myFile.wav", path_or_hf_repo="mlx-community/whisper-large-v3-mlx")
    #text = mlx_whisper.transcribe(audio_file)["text"]
    print("The result is:")
    print(result)
    return result["text"]
  except Exception as e:
    print(e)
    return
