from boggle import Boggle
from flask import Flask, render_template, session

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route('/')
def home():
    board = boggle_game.make_board()
    print('BOARD:', board)
    session['board'] = board
    print('SESSION:', session['board'])
    return render_template('home.html', board=board)
