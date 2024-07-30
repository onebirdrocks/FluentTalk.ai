from deepgram import DeepgramClient, PrerecordedOptions
from functools import wraps
import time

from dotenv import load_dotenv
import os

load_dotenv()
DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')

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


# Hosted sample file
AUDIO_URL = {
  'url': 'https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav'
}

@measure_time
def main():
    deepgram = DeepgramClient(DEEPGRAM_API_KEY)

    options = PrerecordedOptions(
        smart_format=True, model="nova-2", language="en-US"
    )

    response = deepgram.listen.prerecorded.v('1').transcribe_url(AUDIO_URL, options)
    print(response.to_json(indent=4))

if __name__ == '__main__':
    main()