import os
from dotenv import load_dotenv

load_dotenv()

URL = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2"

ACCOUNT_KEY = os.getenv("ACCOUNT_KEY")
HEADERS = {
    "AccountKey": ACCOUNT_KEY 
}


DIRECTUS_URL = "http://directus:8055"
TOKEN = os.getenv("TOKEN")
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