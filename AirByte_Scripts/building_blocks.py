# -- import statments -- #

import requests

# -- Airbyte API URLS -- #

AIRBYTE_PUBLIC_API = "http://localhost:8000/api/public/v1/"
AIRBYTE_API = "http://localhost:8000/api/v1/"


# -- Main Code -- #

def test_connection() -> bool:
    health_url = AIRBYTE_PUBLIC_API + '/health'

    health_response = requests.get(health_url)
    connection_res = health_response.text

    if connection_res == 'Successful operation':
        return True
    
    else:
        return False
    

def get_access_token(client_id: str, client_secret: str) -> str:
    url_token = AIRBYTE_PUBLIC_API + "/applications/token"

    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    try:
        token_response = requests.post(url_token, json=payload, headers=headers)
        token_response.raise_for_status()
        
        return token_response.json()['access_token']
    
    except Exception as e:
        print(e)
        return ""
    
def get_source_definition(source_name: str, token: str) -> str:
    source_def_url = AIRBYTE_API + "/source_definitions/list" 

    headers = {
        "accept": "application/json",
        "Content-Type" : "application/json",
        "authorization" : "Bearer " + token
        } 
    
    try:
        source_def_response = requests.post(source_def_url, headers=headers)
        source_def_response.raise_for_status()
        
        # print(source_def_response.json()['sourceDefinitions'])
        for source_def in source_def_response.json()['sourceDefinitions']:
            # print(source_def['name'])
            # print(source_def['name'].lower())
            if source_name in source_def['name'].lower():
                return source_def['sourceDefinitionId']
            
        raise Exception("source definition not found!")
    
    except Exception as e:
        print(e)
        return ""