import openai
import os
from dotenv import load_dotenv

load_dotenv()

with open("/Users/alp/Documents/alp/llm_api/gpt_api_key.txt", "r") as ff:
    api_key = ff.readline()
openai.api_key = os.getenv(api_key)

def call_gpt(prompt, temperature=0.3, model="gpt-4o"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message["content"]
