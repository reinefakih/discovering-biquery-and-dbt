# -- import statments -- #

import requests
import json

# -- Airbyte API URLS -- #

AIRBYTE_PUBLIC_API = "http://localhost:8000/api/public/v1"
AIRBYTE_API = "http://localhost:8000/api/v1"

# -- Main Code -- #
def create_mysql_dest(dest_definition: str, workspace: str, name: str, project_id, token: str):

    url = AIRBYTE_API + "/destinations/create"

    payload = { 
        "destinationDefinitionId": dest_definition,
        "workspaceId": workspace,

        "connectionConfiguration": {
            "project_id": project_id
        },

        "name": f"BigQuery - {name}"}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer " + token
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        # print(response.json())
        response.raise_for_status()

        print(f"Destination for BigQuery successfully made")
    
    except Exception as e:
        print(f"{e}")