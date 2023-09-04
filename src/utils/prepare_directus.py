import requests
import json
import src.config.config as config

class AuthError(Exception): pass

def prepare_directus(collection, directus_url=config.DIRECTUS_URL, directus_header=config.DIRECTUS_HEADER):

    print(f"\nCreating collection: {collection}")
    
    resp = requests.get(f"{directus_url}/collections/{collection}", headers=directus_header)
    if resp.status_code == 401:
        print(f"INVALID_CREDENTIALS! Please ensure you updated the TOKEN variable in your environment.")
        raise AuthError("INVALID_CREDENTIALS!")

    if resp.status_code not in [200, 204]:
        # Create collection if not exist
        resp_1 = requests.post(f"{directus_url}/collections", headers=directus_header, data=json.dumps({"collection": collection, "schema": {}}))
        if resp_1.status_code not in [200, 204]:
            print(f"Error creating collection {collection} to directus! Error message: {resp_1.text}")
        else:
            print(f"Collection {collection} successfully created!")

        for field in config.FIELD_NAMES:
            resp_2 = requests.post(f"{directus_url}/fields/{collection}", headers=directus_header, data=json.dumps({"field": field, "type": "string", "schema": {}}))

            if resp_2.status_code not in [200, 204]:
                print(f"Error creating field {field} to directus collection {collection}! Error message: {resp_2.text}")
            else:
                print(f"Field: {field} for Collection {collection} successfully created!")
    else:
        print(f"Collection {collection} already present! Skipping creation of collection...")



if __name__ == "__main__":
    prepare_directus("buses")
    prepare_directus("bus_eve")