from datetime import datetime
from zoneinfo import ZoneInfo

def get_arrival_duration(arrival_time):
    if arrival_time == '':
        return -2
    arrival_duration = (datetime.strptime(arrival_time, '%Y-%m-%dT%H:%M:%S+08:00').timestamp() - datetime.now(ZoneInfo("Singapore")).timestamp()) // 60
    if arrival_duration < 0:
        return -1
    return int((datetime.strptime(arrival_time, '%Y-%m-%dT%H:%M:%S+08:00').timestamp() - datetime.now(ZoneInfo("Singapore")).replace(tzinfo=None).timestamp()) // 60)
