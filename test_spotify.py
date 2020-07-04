import requests
import json

class TestSpotify():

    def test_given_valid_url_check_status_code_equals_200(self):
        response = requests.get("https://api.spotify.com")
        assert response.status_code == 200

    def test_get_current_user_check_status_code_equals_200(self):
        url = 'https://api.spotify.com/v1/me'

        headers = {
            'authorization': 'Bearer BQCRXjNz1ueEuNsyBRih-O1JEtWDc9_6T47v2YDPNlehfh2EcRi5Olcc3pGs0HeHIB0kvJ-VNf-P-HEHljHsl0u_5oyaaDoAcxFmEawOfpVWWeD9mGr3prf9WTJYhJjr8nuOuD_bqxJvtIgH3vjAPnwHlnS0hyBLNjegOiuyqI19pfK5PVzreBVIS5aGkelYleIqh_C9FzzSTGP23acDVV59VcRHjJurhEbxir8oH_bqUR_5U7yYdtYYI7pNQ-vqy4lYt2NCneClyF_kVhbVcD5HVkU3vZGv',
            'cache-control': 'no-cache'
        }

        response = requests.get( url, headers=headers)
        # Validate response headers and body contents, e.g. status code.
        assert response.status_code == 200





    
