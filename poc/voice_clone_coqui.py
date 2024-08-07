import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
wav = tts.tts(text="Hello world!", speaker_wav="media/trump.wav", language="en")


# Text to speech to a file
speech_dream = """
I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal." I have a dream that one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood. I have a dream that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice.
I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character. I have a dream today!
I have a dream that one day, down in Alabama, with its vicious racists, with its governor having his lips dripping with the words of "interposition" and "nullification" -- one day right there in Alabama is going to be transformed into a state that is justly governed by men who support the Constitution.
"""

speech_car = """
There is one more thing......I have an important announcement to make. We are appointing Mr. Yongfeng Wu as the leader to spearhead our Apple Car initiative. This will be an extraordinary vehicle, one that I am confident will surpass competitors like Tesla, Xiaomi, NIO, and Xpeng. I pledge that on the day this car rolls off the production line, every member of the Touchstone team will receive one as a gift from Apple. Trust me, it's something only Apple can do.
"""

intro_echofluent ="""
EchoFluent is an experimental and educational Skunkworks project developed during my spare time at WeWork Hangzhou. Initially named FluentTalk.AI, the project's name was inspired by a delightful coincidence during my stay: I was warmly welcomed by a lovely WeWork staff member named Echo, which sparked the idea for EchoFluent.

The project is named after Echo, the Greek goddess known for her ability to echo and repeat others. Just like Echo, language learning thrives on repeated listening and speaking practice, helping you become more fluent over time.

EchoFluent aims to create an AI-powered voice tutor application that offers personalized, interactive, and offline language learning experiences in multiple languages. This initial version is a proof of concept, with continuous improvements and enhancements planned for the future. My goal is to keep EchoFluent simple and efficient while expanding its capabilities.
"""

## I hava a dream
tts.tts_to_file(text=speech_dream , speaker_wav="media/tim_cook.wav", language="en", file_path="output/tim_dream.wav")
tts.tts_to_file(text=speech_dream , speaker_wav="media/trump.wav", language="en", file_path="output/trump_dream.wav")
tts.tts_to_file(text=speech_dream , speaker_wav="media/rym.wav", language="en", file_path="output/rym_dream.wav")


## Apple care
tts.tts_to_file(text=speech_car , speaker_wav="media/tim_cook.wav", language="en", file_path="output/tim_car.wav")
tts.tts_to_file(text=speech_car , speaker_wav="media/trump.wav", language="en", file_path="output/trump_car.wav")
tts.tts_to_file(text=speech_car , speaker_wav="media/rym.wav", language="en", file_path="output/rym_car.wav")

## EchoFluent
tts.tts_to_file(text=intro_echofluent , speaker_wav="media/tim_cook.wav", language="en", file_path="output/tim_echo.wav")
tts.tts_to_file(text=intro_echofluent , speaker_wav="media/trump.wav", language="en", file_path="output/trump_echo.wav")
tts.tts_to_file(text=intro_echofluent , speaker_wav="media/rym.wav", language="en", file_path="output/rym_echo.wav")

