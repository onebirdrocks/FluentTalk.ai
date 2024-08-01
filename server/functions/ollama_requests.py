import ollama
from functions.database import get_recent_messages




def get_chat_response(message_input):

  messages = get_recent_messages()
  user_message = {"role": "user", "content": message_input + " Only say two or 3 words in Chinese if speaking in Chinese. The remaining words should be in English"}
  messages.append(user_message)
  print(messages)

  try:
    response = ollama.chat(model='llama3', messages=messages)
    print("result from ollama:")
    print(response['message']['content'])
    return response['message']['content']
  except Exception as e:
    return