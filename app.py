from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route('/')
def home():
    '''
    home is responsible for initializing the board and other
    session variables for the player. It then uses those variables
    to render the game.
    '''
    board = boggle_game.make_board()
    print('BOARD:', board)
    session['board'] = board
    print('SESSION:', session['board'])
    session['score'] = 0
    if 'high_score' not in session:
        session['high_score'] = 0
    if 'num_played' not in session:
        session['num_played'] = 0
    return render_template('home.html',
        board=board,
        high_score=session['high_score'],
        times_played=session['num_played'])

@app.route('/submit', methods=["POST"])
def submit():
    '''
    submit receives a guess that the user entered on the frontend. It checks
    if the word guessed is on the board. If it is on the board it updates the
    player's score. It returns both the result and new score so that the
    frontend can be updated.
    '''
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

@app.route('/score', methods=["POST"])
def score():
    '''
    score receives the score stored on the frontend and updates
    the players high score if the new score is higher. It also udpates
    the number of games the player has played.
    '''
    score = int(request.json.get('score', ''))
    if score > session['high_score']:
        session['high_score'] = score
    session['num_played'] = session['num_played'] + 1
    print('submitted score: %s, high score: %s, times played: %s' %
        (score, session['high_score'], session['num_played']))
    return jsonify('')
