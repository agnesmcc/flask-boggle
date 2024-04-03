from boggle import Boggle
from flask import Flask, render_template

boggle_game = Boggle()

app = Flask(__name__)

@app.route('/')
def home():
    board = boggle_game.make_board()
    print(board)
    return render_template('home.html', board=board)
