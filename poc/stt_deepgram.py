from deepgram import DeepgramClient, PrerecordedOptions
from dotenv import load_dotenv
import os

from measure_time import measure_time 

load_dotenv()
DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')


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