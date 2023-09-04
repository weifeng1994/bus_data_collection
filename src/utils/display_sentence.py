def display_sentences(bus_stop_code, service_no, arrival_duration_1, arrival_duration_2, load_1, load_2, type_1, type_2):
    if not arrival_duration_1 or arrival_duration_1 == -2:
        return f"There is no estimate for bus {service_no} at bus stop {bus_stop_code}"
    elif not arrival_duration_2 or arrival_duration_2 == -2:
        return f"Bus {service_no} is arriving bus stop {bus_stop_code} in {arrival_duration_1} mins (Load: {load_1}, Type: {type_1}), no estimate for subsequent bus"
    elif arrival_duration_1 >= 1 and arrival_duration_2 >= 1:
        return f"Bus {service_no} is arriving bus stop {bus_stop_code} in {arrival_duration_1} mins (Load: {load_1}, Type: {type_1}), subsequent bus in {arrival_duration_2} mins (Load: {load_2}, Type: {type_2})"
    elif arrival_duration_1 == 0 and arrival_duration_2 >= 1:
        return f"Bus {service_no} is arriving bus stop {bus_stop_code} NOW (Load: {load_1}, Type: {type_1}), subsequent bus in {arrival_duration_2} mins (Load: {load_2}, Type: {type_2})"
    elif arrival_duration_1 < 0 and arrival_duration_2 >= 1:
        return f"Bus {service_no} has already left bus stop {bus_stop_code}, next bus is arriving in {arrival_duration_2} mins (Load: {load_2}, Type: {type_2})"
    elif arrival_duration_1 < 0 and arrival_duration_2 == 0:
        return f"Bus {service_no} has already left bus stop {bus_stop_code}, next bus is arriving NOW (Load: {load_2}, Type: {type_2})"
    elif arrival_duration_1 < 0 and arrival_duration_2 < 0:
        return f"Bus {service_no} has already left bus stop {bus_stop_code}, please check again in 1 minute time!"
