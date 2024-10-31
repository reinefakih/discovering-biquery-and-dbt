# -- import statments -- #

import requests
import json

# -- Airbyte API URLS -- #

AIRBYTE_PUBLIC_API = "http://localhost:8000/api/public/v1"
AIRBYTE_API = "http://localhost:8000/api/v1"

# -- Main Code -- #

def create_google_sheets_source(source_name: str, spreadsheet_id: str, auth_type: str, credentials: dict, source_definition: str, workspace: str, token: str):
    url = AIRBYTE_API + "/sources/create"

    payload = {
        "name": f"Google Sheets - {source_name}",
        "workspaceId": workspace,
        "sourceDefinitionId": source_definition,
        "connectionConfiguration": {
            "spreadsheet_id": spreadsheet_id,
            "credentials": {
                'auth_type': auth_type,
                "service_account_info": str(credentials)}
        }
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

        print(f"Source for Google Sheets - {source_name} source successfully made")
    
    except Exception as e:
        print(response.text)
        print(f"{e}")
