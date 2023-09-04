import requests
import json
import src.config.config as config

def upload_to_directus(data, collection):
    resp = requests.post(f"{config.DIRECTUS_URL}/items/{collection}", headers=config.DIRECTUS_HEADER, data=json.dumps(data))
    if resp.status_code not in [200, 204]:
        print(f"Error uploading data to directus {collection}! Error message: {resp.text}")