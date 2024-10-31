from building_blocks import test_connection, get_access_token, get_source_definition
from source import create_google_web_fonts_source
import os
from dotenv import load_dotenv, find_dotenv
import json
# -- Import Local Environmental Variables -- #

load_dotenv(find_dotenv(), override=True)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECERT = os.getenv('CLIENT_SECRET')
WORK_SPACE = os.getenv('WORKSPACE_ID')
WF_KEY = os.getenv('WF_API_KEY')
# print(test_connection())

TOKEN = get_access_token(CLIENT_ID, CLIENT_SECERT)
SOURCE_DEF = get_source_definition('google webfonts', TOKEN)
connected = test_connection()

if connected and (TOKEN != "") and (SOURCE_DEF != ""):
    create_google_web_fonts_source("api_test", WF_KEY, SOURCE_DEF, WORK_SPACE, TOKEN)

else:
    "Something went wrong"