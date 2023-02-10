# #########################################################
# ChatGPT CLI
# #########################################################
import sys
import openai
import os
import getpass

# Set the API key and some initial parameter values
api_key = "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"
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
