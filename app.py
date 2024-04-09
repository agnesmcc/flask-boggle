from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route('/')
def home():
    board = boggle_game.make_board()
    print('BOARD:', board)
    session['board'] = board
    print('SESSION:', session['board'])
    session['score'] = 0
    return render_template('home.html', board=board)

@app.route('/submit', methods=["POST"])
def submit():
    guess = request.args.get('guess', '')
    print(guess)

    board = session['board']
    is_valid = boggle_game.check_valid_word(board, guess)

    if is_valid == 'ok':
        score = session.get('score')
        session['score'] = score + len(guess)
        print(session['score'])

    response = {'result': is_valid, 'score': session['score']}
    print(response)
    return jsonify(response)
