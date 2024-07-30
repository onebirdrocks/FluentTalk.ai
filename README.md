# FluentTalk.ai
An AI-powered English tutor designed to help you practice and improve your English speaking skills. This locally running application leverages advanced language models to provide personalized and interactive speaking exercises, feedback, and guidance, making language learning both effective and enjoyable.

# Installation
```

pip install ollama
pip install mlx
pip install openai-whisper
pip install mlx-whisper

pip install python-dotenv


pip install pyobjc
#https://pypi.org/project/pyttsx3/
pip install pyttsx3

```

# PoC

python whisper_poc.py Bueller-Life-moves-pretty-fast.wav
```
python whisper_poc.py Bueller-Life-moves-pretty-fast.wav

/opt/miniconda3/envs/wework/lib/python3.10/site-packages/whisper/__init__.py:146: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  checkpoint = torch.load(fp, map_location=device)
-------------------------------------
 Running audio_to_text_mlx function
-------------------------------------
Fetching 3 files: 100%|███████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 33644.15it/s]
The result is: Yep, I said it before and I'll say it again. Life moves pretty fast. You don't stop and look around once in a while. You could miss it.
Function 'audio_to_text_mlx' took 3.6788 seconds to complete.
-------------------------------------
 Running audio_to_text function
-------------------------------------
The result is: yep I said it before and I'll say it again life moves pretty fast you don't stop and look around once in a while you could miss it
Function 'audio_to_text' took 6.3204 seconds to complete.
```


python
```
python deepgram_poc.py
/Users/onebird/github/FluentTalk.ai/deepgram_poc.py:33: DeprecatedWarning: prerecorded is deprecated as of 3.4.0 and will be removed in 4.0.0. deepgram.listen.prerecorded is deprecated. Use deepgram.listen.rest instead.
  response = deepgram.listen.prerecorded.v('1').transcribe_url(AUDIO_URL, options)
{
    "metadata": {
        "transaction_key": "deprecated",
        "request_id": "072b5403-f119-4364-b5fa-042093cdb3f0",
        "sha256": "5324da68ede209a16ac69a38e8cd29cee4d754434a041166cda3a1f5e0b24566",
        "created": "2024-07-30T07:40:57.048Z",
        "duration": 17.566313,
        "channels": 1,
        "models": [
            "30089e05-99d1-4376-b32e-c263170674af"
        ],
        "model_info": {
            "30089e05-99d1-4376-b32e-c263170674af": {
                "name": "2-general-nova",
                "version": "2024-01-09.29447",
                "arch": "nova-2"
            }
        }
    },
    "results": {
        "channels": [
            {
                "alternatives": [
                    {
                        "transcript": "Yep. I said it before and I'll say it again. Life moves pretty fast. You don't stop and look around once in a while, you could miss it.",
                        "confidence": 0.9982273,
                        "words": [
                            {
                                "word": "yep",
                                "start": 5.52,
                                "end": 6.02,
                                "confidence": 0.9985875,
                                "punctuated_word": "Yep."
                            },
                            {
                                "word": "i",
                                "start": 7.095,
                                "end": 7.2549996,
                                "confidence": 0.8246852,
                                "punctuated_word": "I"
                            },
                            {
                                "word": "said",
                                "start": 7.2549996,
                                "end": 7.415,
                                "confidence": 0.9356652,
                                "punctuated_word": "said"
                            },
                            {
                                "word": "it",
                                "start": 7.415,
                                "end": 7.495,
                                "confidence": 0.9983712,
                                "punctuated_word": "it"
                            },
                            {
                                "word": "before",
                                "start": 7.495,
                                "end": 7.975,
                                "confidence": 0.9997557,
                                "punctuated_word": "before"
                            },
                            {
                                "word": "and",
                                "start": 7.975,
                                "end": 8.135,
                                "confidence": 0.56372404,
                                "punctuated_word": "and"
                            },
                            {
                                "word": "i'll",
                                "start": 8.135,
                                "end": 8.295,
                                "confidence": 0.9982273,
                                "punctuated_word": "I'll"
                            },
                            {
                                "word": "say",
                                "start": 8.295,
                                "end": 8.455,
                                "confidence": 0.9986798,
                                "punctuated_word": "say"
                            },
                            {
                                "word": "it",
                                "start": 8.455,
                                "end": 8.615,
                                "confidence": 0.9985266,
                                "punctuated_word": "it"
                            },
                            {
                                "word": "again",
                                "start": 8.615,
                                "end": 9.115,
                                "confidence": 0.8460276,
                                "punctuated_word": "again."
                            },
                            {
                                "word": "life",
                                "start": 9.975,
                                "end": 10.295,
                                "confidence": 0.9956418,
                                "punctuated_word": "Life"
                            },
                            {
                                "word": "moves",
                                "start": 10.295,
                                "end": 10.695,
                                "confidence": 0.9985448,
                                "punctuated_word": "moves"
                            },
                            {
                                "word": "pretty",
                                "start": 10.695,
                                "end": 11.014999,
                                "confidence": 0.9993729,
                                "punctuated_word": "pretty"
                            },
                            {
                                "word": "fast",
                                "start": 11.014999,
                                "end": 11.514999,
                                "confidence": 0.9992909,
                                "punctuated_word": "fast."
                            },
                            {
                                "word": "you",
                                "start": 11.975,
                                "end": 12.215,
                                "confidence": 0.9474219,
                                "punctuated_word": "You"
                            },
                            {
                                "word": "don't",
                                "start": 12.215,
                                "end": 12.455,
                                "confidence": 0.99980575,
                                "punctuated_word": "don't"
                            },
                            {
                                "word": "stop",
                                "start": 12.455,
                                "end": 12.695,
                                "confidence": 0.999828,
                                "punctuated_word": "stop"
                            },
                            {
                                "word": "and",
                                "start": 12.695,
                                "end": 12.855,
                                "confidence": 0.9984738,
                                "punctuated_word": "and"
                            },
                            {
                                "word": "look",
                                "start": 12.855,
                                "end": 13.014999,
                                "confidence": 0.99972683,
                                "punctuated_word": "look"
                            },
                            {
                                "word": "around",
                                "start": 13.014999,
                                "end": 13.334999,
                                "confidence": 0.9994728,
                                "punctuated_word": "around"
                            },
                            {
                                "word": "once",
                                "start": 13.334999,
                                "end": 13.575,
                                "confidence": 0.99803597,
                                "punctuated_word": "once"
                            },
                            {
                                "word": "in",
                                "start": 13.575,
                                "end": 13.735,
                                "confidence": 0.997106,
                                "punctuated_word": "in"
                            },
                            {
                                "word": "a",
                                "start": 13.735,
                                "end": 13.815,
                                "confidence": 0.9540977,
                                "punctuated_word": "a"
                            },
                            {
                                "word": "while",
                                "start": 13.815,
                                "end": 14.315,
                                "confidence": 0.9718098,
                                "punctuated_word": "while,"
                            },
                            {
                                "word": "you",
                                "start": 14.561313,
                                "end": 14.7213125,
                                "confidence": 0.98999095,
                                "punctuated_word": "you"
                            },
                            {
                                "word": "could",
                                "start": 14.7213125,
                                "end": 14.961312,
                                "confidence": 0.9966581,
                                "punctuated_word": "could"
                            },
                            {
                                "word": "miss",
                                "start": 14.961312,
                                "end": 15.461312,
                                "confidence": 0.997384,
                                "punctuated_word": "miss"
                            },
                            {
                                "word": "it",
                                "start": 17.281313,
                                "end": 17.566313,
                                "confidence": 0.9900374,
                                "punctuated_word": "it."
                            }
                        ],
                        "paragraphs": {
                            "transcript": "\nYep. I said it before and I'll say it again. Life moves pretty fast. You don't stop and look around once in a while, you could miss it.",
                            "paragraphs": [
                                {
                                    "sentences": [
                                        {
                                            "text": "Yep.",
                                            "start": 5.52,
                                            "end": 6.02
                                        },
                                        {
                                            "text": "I said it before and I'll say it again.",
                                            "start": 7.095,
                                            "end": 9.115
                                        },
                                        {
                                            "text": "Life moves pretty fast.",
                                            "start": 9.975,
                                            "end": 11.514999
                                        },
                                        {
                                            "text": "You don't stop and look around once in a while, you could miss it.",
                                            "start": 11.975,
                                            "end": 17.566313
                                        }
                                    ],
                                    "start": 5.52,
                                    "end": 17.566313,
                                    "num_words": 28
                                }
                            ]
                        }
                    }
                ]
            }
        ]
    }
}
Function 'main' took 2.9626 seconds to complete.
```
