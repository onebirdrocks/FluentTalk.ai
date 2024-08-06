import os
import json
import random

local_file="chat_history.json"

# Save messages for retrieval later on
def get_recent_messages():

  # Define the file name
  file_name = local_file
  learn_instruction = {"role": "system", 
                       "content": "You are an English teacher named Echo. The user is named Yiming. Keep your responses under 30 words. If you find any grammatical error in user's messages. Please correct him and make the response less than 30 words."}
  
  messages = []

  x = random.uniform(0, 1)
  if x < 0.2:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will have some light humour. "
  elif x < 0.5:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will include some topics related to GenAI, new technologies, life styles, and more."
  else:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will recommend some related Englishs word to learn (Related to your topics)."

  messages.append(learn_instruction)


  # Get last messages
  try:
    with open(file_name) as user_file:
      data = json.load(user_file)
      
      # Append last 5 rows of data
      if data:
        if len(data) < 5:
          for item in data:
            messages.append(item)
        else:
          for item in data[-5:]:
            messages.append(item)
  except:
    pass

  
  # Return messages
  return messages


# Save messages for retrieval later on
def store_messages(request_message, response_message):

  # Define the file name
  file_name = local_file

  # Get recent messages
  messages = get_recent_messages()[1:]

  # Add messages to data
  user_message = {"role": "user", "content": request_message}
  assistant_message = {"role": "assistant", "content": response_message}
  messages.append(user_message)
  messages.append(assistant_message)

  # Save the updated file
  with open(file_name, "w") as f:
    json.dump(messages, f)


# Save messages for retrieval later on
def reset_messages():

  # Define the file name
  file_name = local_file

  # Write an empty file
  open(file_name, "w")
