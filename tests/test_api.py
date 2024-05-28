# tests/test_api.py

import unittest
import time
from main import api 
#from main import get_token_oauth2
#from main import get_authorization _code
#from main import exchange_code_for_token


class test_api(unittest.TestCase):
        
    def test_navigation(self):
        #token=get_token_oauth2('TU_CLIENT_ID','TU_CLIENT_SECRET', 'https://api.ejemplo.com/oauth2/token')
        #codigo_autorizacion = get_authorization _code(client_id, redirect_uri, authorization_url)
        #token = exchange_code_for_token(client_id, client_secret, redirect_uri, codigo_autorizacion, token_url)
        api(self,"tokenExample")
        
if __name__ == "__main__":
    unittest.main()
