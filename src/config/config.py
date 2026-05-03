import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")

ACCOUNT_KEY = os.getenv("ACCOUNT_KEY")
HEADERS = {
    "AccountKey": ACCOUNT_KEY 
}

DIRECTUS_URL = os.getenv("DIRECTUS_URL")
res = requests.post(f"{DIRECTUS_URL}/auth/login", json={
        "email": os.getenv("ADMIN_EMAIL"),
        "password": os.getenv("ADMIN_PASSWORD")
    })
TOKEN = res.json()["data"]["access_token"]

# TOKEN = os.getenv("ADMIN_TOKEN")
DIRECTUS_HEADER = {
    "Authorization": f"Bearer {TOKEN}",
    'Content-Type': 'application/json'
}

FIELD_NAMES = ['ServiceNo', 'NextBus_EstimatedArrival', 'NextBus_Latitude',
       'NextBus_Longitude', 'NextBus_Load', 'NextBus_Type',
       'NextBus2_EstimatedArrival', 'NextBus2_Latitude', 'NextBus2_Longitude',
       'NextBus2_Load', 'NextBus2_Type', 'NextBus3_EstimatedArrival',
       'NextBus3_Latitude', 'NextBus3_Longitude', 'NextBus3_Load',
       'NextBus3_Type', 'Timestamp', 'NextBus_EstimatedArrivalDuration',
       'NextBus2_EstimatedArrivalDuration',
       'NextBus3_EstimatedArrivalDuration', 'BusStopCode']