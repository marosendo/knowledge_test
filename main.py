# main.py

from config.config import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import requests

def navigate_menus(driver,section):
    # Navigate to the website
    driver.get("https://bcncgroup.com/")

    # Wait up to 10 seconds for the element to be visible
    home = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, section)))
    time.sleep(5)
    home.click()
  
def readParagraph(driver):
    # Print the text list
    paragraf = driver.find_elements(By.CSS_SELECTOR,"div.text>p")
    for text in paragraf:
        actions = ActionChains(driver)
        actions.move_to_element(text).perform()
        print(text.text)

def api(self,token):
    #Add example OAuth 2.0
    """
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(https://jsonplaceholder.typicode.com/albums, headers=headers)
    """
    response = requests.get("https://jsonplaceholder.typicode.com/albums")
    json_data = response.json()
    
    with open('resources/albums.json', 'r') as file:
        data = json.load(file)
            
        titles = [item['title'] for item in data if 'title' in item]
        titlesJson = [item['title'] for item in json_data if 'title' in item]

        for title,titleJs in zip(titles, titlesJson):
            self.assertEqual(title,titleJs)      
"""           
def get_token_oauth2(client_id, client_secret, token_url):
    payload = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=payload, auth=(client_id, client_secret))
    
    if response.status_code == 200:
        token = response.json().get('access_token')
        return token
    else:
        response.raise_for_status()
        
def get_authorization _code(client_id, redirect_uri, authorization_url):
    parametros = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'response_type': 'code'
    }
    url_autorizacion = authorization_url + '?' + urlencode(parametros)
    print("Please visit the following URL and authorize the application")
    print(url_autorizacion)
    code = input("Enter the authorization code:")
    return code
    
def exchange_code_for_token(client_id, client_secret, redirect_uri, code, token_url):
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(token_url, data=payload)
    
    if response.status_code == 200:
        token = response.json().get('access_token')
        return token
    else:
        response.raise_for_status() 
"""  
if __name__ == "__main__":
    driver = get_driver()
    
    try:
        navigate_menus(driver,"test")
    finally:
        driver.quit()
