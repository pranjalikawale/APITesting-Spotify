import requests
import json
import pytest

class TestSpotify():
    token=''
    playlists=[]
    total_playlist=0
    track_id=[]
    user_id = ''
    user_name=''

    @pytest.fixture
    def spotify_token(self):
        token='Bearer BQBSQDVBoTGBKTxj0tcNys380EU91c26EisYkiRwm2Y1PTy0S3SGlkTgywYTffzyk_aS8P19Xz0NkcrH8wr4drd4rfcE4JZazIqQvWXkDB3dI2SRutFiiI0LuDTJD4VoKwjRNOidZu28wSz8-ITCRPhGVkmqO17YIalCC_EUZc--NZFxMyYyl_pRAqRmotN72TleCok5Ot7uW3wL6TF3ZFo__LszFEu8CN5kY-8Pjo2Yau_sXmSd40liqmJo9gpBQQkNdA9IRHVuP6AKIswm9mwrpsdBAR_a'
        headers = {
            'authorization': token ,
            'cache-control': 'no-cache',
            'Content-Type':'application/json'
        }
        return headers

    def test_given_valid_url_check_status_code_equals_200(self):
        response = requests.get("https://api.spotify.com")
        assert response.status_code == 200
       
    def test_get_user_id(self,spotify_token):
        url = 'https://api.spotify.com/v1/me'

        response = requests.get( url, headers=spotify_token)
        # Validate response headers and body contents, e.g. status code.
        response_body=response.json()
        global user_id
        user_id=response_body['id']
        assert user_id == 'y4qylmcub7wbtqwg9pqyyz652' and response.status_code == 200
        print(user_id)

    def test_get_user_name(self,spotify_token):
        global user_name
        url = 'https://api.spotify.com/v1/me'

        response = requests.get( url, headers=spotify_token)
        # Validate response headers and body contents, e.g. status code.
        response_body=response.json()
        user_name=response_body['display_name']
        assert user_name == "Pranjali Kawale" and response.status_code == 200
        print(user_name)

    def test_get_user_profile(self,spotify_token):
        global user_id
        url = 'https://api.spotify.com/v1/users/'+user_id+'/'

        response = requests.get( url, headers=spotify_token)
        # Validate response headers and body contents, e.g. status code.
        response_body=response.json()
        assert response.status_code == 200
        print(json.dumps(response_body))    

    def test_get_current_user_check_status_code_equals_401(self):
        url = 'https://api.spotify.com/v1'

        headers = {
            'authorization': 'Bearer BQA8zZrYeKtkDEox5BN-U1iqdMsZeIcBlZkBmoTTmUl_pjgn1PnDucUQ9b8cm6BrexH-tl6hMNLBilpmJdSpq0xJ6qjxCKfygxAco_FSV50yAhMV4IadA6XAJJQSkPp-noRgnupd_x0ZuvusY1-OcTHL3LxtTT9R-TeU0Mq4eilj--P-vKaS2B3SZh72KAhCW0GFvZamspmZiRGaddvVIzQeXUM0iQrNYUECFVCsdA3v9KLJnSxqp9QsSTeoeFNGbLCuogQ2pZfTm7si0dr0JIuwpLT5a6_S'
        }

        response = requests.get( url, headers=headers)
        # Validate response headers and body contents, e.g. status code.
        assert response.status_code == 401
    
    def test_create_playlist(self,spotify_token):
        global user_id
        url = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'
        payload = {'name': 'Pranjali', 'description': 'New playlist description','public': True}

        response = requests.post( url, headers=spotify_token,data=json.dumps(payload))
        # Validate response headers and body contents, e.g. status code.
        response_body=response.json()
        assert response_body['name'] == 'Pranjali' and response.status_code == 201
        print(json.dumps(response_body))    
    
    def test_get_user_playlist_info(self,spotify_token):
        global user_id,total_playlist
        url = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'

        response = requests.get( url, headers=spotify_token)
        # Validate response headers and body contents, e.g. status code.
        response_body=response.json()
        total_playlist=response_body['total']
        assert response.status_code == 200
        print(total_playlist)
        print(json.dumps(response_body)) 

    def test_get_user_playlist(self,spotify_token):
        global user_id,total_playlist
        url = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'

        response = requests.get( url, headers=spotify_token)
        # Validate response headers and body contents, e.g. status code.
        response_body=response.json()
        total_playlist=response_body['total']
        playlists =[total_playlist]
        for counter in range(total_playlist,1):
            playlists[counter] = response_body['items[' + counter + '].id'] #get playlist id
        assert response.status_code == 200
        for id in playlists:
            print("PlayList Id" + str(id))
        print(json.dumps(response_body))    



    
