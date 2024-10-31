# -- import statments -- #

import requests

# -- Airbyte API URLS -- #

AIRBYTE_PUBLIC_API = "http://localhost:8000/api/public/v1"
AIRBYTE_API = "http://localhost:8000/api/v1"

# -- Main Code -- #

def create_google_web_fonts_source(source_name: str, api_key: dict, source_definition: str, workspace: str, token: str):
    url = AIRBYTE_API + "/sources/create"

    payload = {
        "sourceDefinitionId": source_definition,
        "workspaceId": workspace,
        "connectionConfiguration":{
            "api_key": api_key
        },
        "name": "Google Web Fonts " + source_name
    }

    headers = {
        "accept": "application/json",
        "Content-Type" : "application/json",
        "authorization" : "Bearer " + token
    } 

    try:
        response = requests.post(url, json=payload, headers=headers)
        # print(response.json())
        response.raise_for_status()

        print(f"Source for Google Web Font - {source_name} successfully made")
    
    except Exception as e:
        print(f"{e}")
