from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
import json

class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_home(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['high_score'] = 3
                change_session['num_played'] = 4

            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<span id="player-high-score">%s' % session['high_score'], html)
            self.assertIn('<span id="player-num-played">%s' % session['num_played'], html)

    def test_submit(self):
        with app.test_client() as client:
            resp = client.get("/")
            with client.session_transaction() as change_session:
                change_session['board'] = [
                    ['A', 'A', 'A', 'A', 'A'],
                    ['A', 'A', 'A', 'A', 'A'],
                    ['A', 'A', 'A', 'A', 'A'],
                    ['A', 'A', 'A', 'A', 'A'],
                    ['A', 'A', 'A', 'A', 'A'],
                ]

            resp = client.post("/submit?guess=abarticulation")
            resp_json = json.loads(resp.get_data())

            self.assertEqual(resp.status_code, 200)
            self.assertEqual('not-on-board', resp_json['result'])
            self.assertEqual(0, resp_json['score'])

            resp = client.post("/submit?guess=a")
            resp_json = json.loads(resp.get_data())

            self.assertEqual(resp.status_code, 200)
            self.assertEqual('ok', resp_json['result'])
            self.assertEqual(1, resp_json['score'])

    def test_score(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['high_score'] = 1
                change_session['num_played'] = 5

            resp = client.post("/score", json={'score': 0})
            self.assertEqual(session['high_score'], 1)
            self.assertEqual(session['num_played'], 6)

            resp = client.post("/score", json={'score': 6})
            self.assertEqual(session['high_score'], 6)
            self.assertEqual(session['num_played'], 7)

