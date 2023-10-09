import openai
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("API_KEY")

def get_completion(prompt):    
    messages = [ { "role": "user", "content": prompt }]
    response = openai.ChatCompletion.create(
        model = os.getenv("MODEL"),
        messages = messages,
        temperature = 0,
    )
    return response.choices[0].message["content"]