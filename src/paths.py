import random

from flask import render_template, request

from src import app


@app.route('/')
def index():
    """This is the index route
    """
    data = {
        'title': 'Flask App',
        'description': 'This is a simple flask app',
        'articles': [ "title1", "title2", "title3" ],
    }
    return render_template('/views/index.html', data=data)

@app.route('/about')
def about():
    """This is the about route
    """
    about_data = {
        'title': 'About',
        'description': 'This is the about page'
    }
    return render_template('/views/about.html', data=about_data)

@app.route('/form', methods=['GET', 'POST'])
def form():
    """This is form route

    description: This route is used to render the form.html file
        - GET
        - POST
    """
    if request.method == 'GET':
        return render_template('/views/form.html')

    if request.method == 'POST':
        req = request.form['name']
        print('Name:', req)
        return f'Form POST Method: {req}'

    return render_template('/views/form.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    """This is the game route

    description: This route is used to Rock-Paper-Scissors game
        - GET
            - choose your hand
                - rock: 0
                - paper: 1
                - scissors: 2
        - POST
    """
    if request.method == 'GET':
        return render_template('/views/game.html')

    if request.method == 'POST':
        user_hand = int(request.form['hand'])
        hand_type = {
            0: 'rock',
            1: 'paper',
            2: 'scissors'
        }
        computer_hand = random.randint(0, 2)

        result = (user_hand - computer_hand) % 3
        if result == 0:
            result_str = 'Draw'
        elif result == 1:
            result_str = 'Win'
        else:
            result_str = 'Lose'

        # return f'User: {hand_type[user_hand]},<br />\
        #         Computer: {hand_type[computer_hand]},<br />\
        #         Result: {result_str}'

        result_data = {
            'user': hand_type[user_hand],
            'computer': hand_type[computer_hand],
            'result': result_str
        }

        return render_template('/views/game_result.html', data=result_data)
