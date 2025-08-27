from flask import Flask, request
from random import randint, choice
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    phrases: list[str] = ['Welcome to this page!', 'Hello there!', 'Greetings!']
    return {'phrase': choice(phrases), 'date': datetime.now()}


@app.route('/api/random')
def random():
    number_input: int = request.args.get('number', type = int)
    text_input: str = request.args.get('text_format', type = str, default = 'default_text')
    
    if isinstance(number_input, int):
        return{
            'input': number_input,
            'random_number': randint(0, number_input),
            'text': text_input,
            'date': datetime.now().isocalendar()
        }

    else:
        return {
            'error': 'Invalid input- Please provide a valid number.',
            'date': datetime.now()
        }

if __name__ == '__main__':
    app.run(debug=True)