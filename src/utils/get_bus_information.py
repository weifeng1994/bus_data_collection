import requests
from datetime import datetime
from zoneinfo import ZoneInfo
import pandas as pd
import src.config.config as config
from src.utils.display_sentence import display_sentences
from src.utils.get_arrival_duration import get_arrival_duration

def get_bus_information(bus_stop_code, service_no):
    params = {
        "BusStopCode": bus_stop_code,
        "ServiceNo": service_no
    }

    resp = requests.get(config.URL, headers=config.HEADERS, params=params)
    data = resp.json()

    data = pd.json_normalize(resp.json()['Services'], sep="_")
    if data.empty:
        print(display_sentences(bus_stop_code, service_no, None, None, None, None, None, None))
        return {}
    
    columns_to_keep = ['ServiceNo', 'NextBus_EstimatedArrival', 'NextBus_Latitude', 'NextBus_Longitude', 'NextBus_Load', 'NextBus_Type',
                    'NextBus2_EstimatedArrival', 'NextBus2_Latitude', 'NextBus2_Longitude', 'NextBus2_Load', 'NextBus2_Type',
                    'NextBus3_EstimatedArrival', 'NextBus3_Latitude', 'NextBus3_Longitude', 'NextBus3_Load', 'NextBus3_Type']

    filtered_data = data[columns_to_keep].copy()

    filtered_data['Timestamp'] = datetime.now(ZoneInfo("Singapore")).strftime('%Y-%m-%dT%H:%M:%S+08:00')
    filtered_data['NextBus_EstimatedArrivalDuration'] = filtered_data['NextBus_EstimatedArrival'].apply(get_arrival_duration)
    filtered_data['NextBus2_EstimatedArrivalDuration'] = filtered_data['NextBus2_EstimatedArrival'].apply(get_arrival_duration)
    filtered_data['NextBus3_EstimatedArrivalDuration'] = filtered_data['NextBus3_EstimatedArrival'].apply(get_arrival_duration)

    filtered_data['BusStopCode'] = bus_stop_code

    final_data = filtered_data.to_dict(orient='records')[0]

    print(display_sentences(bus_stop_code, service_no, final_data.get('NextBus_EstimatedArrivalDuration'), final_data.get('NextBus2_EstimatedArrivalDuration'), final_data.get('NextBus_Load'), final_data.get('NextBus2_Load'), final_data.get('NextBus_Type'), final_data.get('NextBus2_Type')))
    return final_data