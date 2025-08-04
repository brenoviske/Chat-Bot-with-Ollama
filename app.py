# Creating a chat bot by using a third party API in order to complete this project

import requests

def chat(prompt):
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model':'mistral',
            'prompt': prompt,
            'stream': False
        }
    )
    return response.json()['response']

if __name__ == '__main__':
    while True:
        user_input = input('You: ')
        if user_input.lower() in ['exit','quit']:break
        response = chat(user_input)
        print('Bot :',response)