import requests
import json
import pytest

class TestSpotify():
    token=""
    playlists=[]
    total_playlist=0
    track_id=[]
    user_id = ""
    JSON = "application/json"

    @pytest.fixture
    def spotify_token(self):
        token='Bearer BQChPQOx6YvcnUD9EWIwQIlNctTa9jAcF8hVpxo24CMB73x6DBa-IsWYO_CC7vId4WeyNQtcnGZpO_JkQHZVvgbxjfr1ZOD6Y19elLDideYURmwGvvvYqZITlzNGuQwEnVI1ulm_50tKTKbVtEGMscQApsbRHS5l5YhpjI_SIxxLr2AVyzxxN5Y8QN4GDpE9-eFT1S3UBDypvPOYtOD1NhUg-AP4yKJE6QMsdQ1ePBklZ0LboHVT3BhBtbKpPE9NwXxhWAVLl4DZzK_NKWuVf9qZoohBvAI3'
        return token

    def test_given_valid_url_check_status_code_equals_200(self):
        response = requests.get("https://api.spotify.com")
        assert response.status_code == 200
       
    def test_get_user_id(self,spotify_token):
        url = 'https://api.spotify.com/v1/me'

        headers = {
            'authorization': spotify_token ,
            'cache-control': 'no-cache',
            'Content-Type':'application/json'
        }

        response = requests.get( url, headers=headers)
        # Validate response headers and body contents, e.g. status code.
        response_body=response.json()
        user_id=response_body['id']
        assert user_id == 'y4qylmcub7wbtqwg9pqyyz652' and response.status_code == 200
        print(user_id)

    def test_get_current_user_check_status_code_equals_401(self):
        url = 'https://api.spotify.com/v1'

        headers = {
            'authorization': 'Bearer BQA8zZrYeKtkDEox5BN-U1iqdMsZeIcBlZkBmoTTmUl_pjgn1PnDucUQ9b8cm6BrexH-tl6hMNLBilpmJdSpq0xJ6qjxCKfygxAco_FSV50yAhMV4IadA6XAJJQSkPp-noRgnupd_x0ZuvusY1-OcTHL3LxtTT9R-TeU0Mq4eilj--P-vKaS2B3SZh72KAhCW0GFvZamspmZiRGaddvVIzQeXUM0iQrNYUECFVCsdA3v9KLJnSxqp9QsSTeoeFNGbLCuogQ2pZfTm7si0dr0JIuwpLT5a6_S',
            'cache-control': 'no-cache'
        }

        response = requests.get( url, headers=headers)
        # Validate response headers and body contents, e.g. status code.
        assert response.status_code == 401



    
