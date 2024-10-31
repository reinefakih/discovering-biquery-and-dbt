from building_blocks import test_connection, get_access_token, get_source_definition
from source import create_google_sheets_source
import os
from dotenv import load_dotenv, find_dotenv
import json
# -- Import Local Environmental Variables -- #

load_dotenv(find_dotenv(), override=True)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECERT = os.getenv('CLIENT_SECRET')
WORK_SPACE = os.getenv('WORKSPACE_ID')
SERVICE_ACC = os.getenv('SERVICE_ACC')
SPREAD_SHEET = os.getenv('SPREAD_ID')
# print(test_connection())

# print(SPREAD_SHEET)

with open(SERVICE_ACC) as auth_file:
    credentials = json.load(auth_file)

TOKEN = get_access_token(CLIENT_ID, CLIENT_SECERT)
SOURCE_DEF = get_source_definition('google sheets', TOKEN)
connected = test_connection()

if connected and (TOKEN != "") and (SOURCE_DEF != ""):
    create_google_sheets_source("API Test", SPREAD_SHEET, "Service", credentials, SOURCE_DEF, WORK_SPACE, TOKEN)

else:
    "Something went wrong"