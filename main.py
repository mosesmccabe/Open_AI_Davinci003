import os

from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.environ.get('OPENAI_API_KEY')

openai_endpoint = 'https://api.openai.com/v1/completions'

# Models:
# DALL-E: generates and edits images
# Whisper: converts audio to text
# codex: understands and generates code
# moderation: detects safe and unsensitive text
# GPT-3: understands and generates natural language
# GPT-3.5: set of models of that improve upon GPT-3
# GPT-4: the latest and move advanced version of OpenAi's large language model

headers = {
    'Authorization': f'Bearer {api_key}'
}

msg = input('Enter color to be generated: ')

prompt = f"""
    You are a color palette generating assistant that responds to text prompts for color palettes
    Your should generate color palettes that fit the theme, mood, or instructions in the prompt.
    The palettes should be between 2 and 8 colors.

    Q: Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea
    A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

    Q: Convert the following verbal description of a color palette into a list of colors: sage, nature, earth
    A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]


    Desired Format: a JSON array of hexadecimal color codes

    Q: Convert the following verbal description of a color palette into a list of colors: {msg} 
    A:
    """
params = {
    'model': 'text-davinci-003',
    'prompt': prompt,
    'max_tokens': 200
}

response = requests.post(url=openai_endpoint, json=params, headers=headers)

data = response.json()

print(data['choices'][0]['text'])