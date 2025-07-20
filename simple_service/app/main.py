import random

from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def hello():
    return {'message': 'hello'}

@app.get('/random')
def random_string():
    phrases = ['Hello world!', 'How are you?', 'Be strong!', 'You are awesome!', 'Random string!']
    return {'random_phrase': random.choice(phrases)}
