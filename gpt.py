# #########################################################
# ChatGPT CLI
# #########################################################
from pathlib import Path
import sys
import openai
import os
import getpass

# Set the API key
api_key_path = str(Path('~').expanduser()) + '/.key/openai'
api_key = open(api_key_path).readlines()[0].strip()
temperature = 0.5  # 0 to 1
max_tokens = 2000  # max 4000

# Set API key
openai.api_key = api_key

prompt = sys.argv

if (len(sys.argv) > 0):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt[1],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1.0,
        frequency_penalty=0.0,
    )
    presence_penalty = 0.0

    print(response["choices"][0]["text"].strip())
