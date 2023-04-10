import requests as reqs
import openai
import os
from pathlib import Path
import wave
import contextlib
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def gen_response(prompt):
    print('Saadan OpenAI-le päringu...')
    
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}], 
        temperature=0.8
    )

    vastus = res['choices'][0]['message']['content']

    with open('vastus.txt', 'w') as f:
        print('Kirjutan vastuse faili...')
        f.write(vastus)
    #print(f'Vastus: {vastus}\n')

    return vastus

def get_audio(text: str):
    print('Saadan TartuNLP-le päringu...')

    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace('"', "'")

    data = '{"text": "' + text + '", "speaker": "mari", "speed": 1}'
    data = data.encode('utf-8')

    headers = {'accept': 'audio/wav', 'Content-Type': 'application/json; charset=utf-8'}

    res = reqs.post('https://api.tartunlp.ai/text-to-speech/v2', data, headers=headers)
    
    print(f'Response code: {res.status_code}')
    if res.status_code != 200:
        print(res.text)
        print(res.headers)
    else:
        with open('vastus.wav', 'wb') as f:
            print('Kirjutan faili...')
            f.write(res.content)

def get_prev_text():
    text = ""
    with open("vastus.txt") as f:
        text = f.read()

    return text

while True:
    kysymys = input("Mida teada soovid?\n")
    text = gen_response(kysymys)
    get_audio(text)

    directory = Path(__file__).resolve().parent
    fname = os.path.join(directory, "vastus.wav")

    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = round(frames / float(rate))
        print(f'Vastus kestab {duration} sekundit')

    os.system(f'cvlc --play-and-exit {fname}')
    print('\n\n-----\n')
