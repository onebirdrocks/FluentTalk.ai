from deepgram import DeepgramClient, SpeakOptions
from io import BytesIO
from decouple import config


# Eleven Labs
# Convert text to speech
def convert_text_to_speech(message):
    try:
        # STEP 1: Create a Deepgram client using the API key from environment variables
        deepgram = DeepgramClient(api_key=config("DEEPGRAM_API_KEY"))

        # STEP 2: Configure the options (such as model choice, audio configuration, etc.)
        options = SpeakOptions(
            model="aura-asteria-en",
        )

        response = deepgram.speak.v("1").request(message, options)
        audio_data = response.read()
        return audio_data

        #return send_file(
        #    BytesIO(audio_data),
        #    mimetype='audio/mpeg',
        #    as_attachment=True,
        #    attachment_filename='audio.mp3'
        #)

    except Exception as e:
        print(f"Exception: {e}")