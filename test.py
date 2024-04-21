from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


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