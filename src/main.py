# %%
from datetime import datetime
from zoneinfo import ZoneInfo
from src.utils.get_bus_information import get_bus_information
from src.utils.upload_to_directus import upload_to_directus

from src.config.bus_config import SUNDAY_PH_BUS, SAT_BUS, WEEKDAY_BUS, PH_EVE_BUS
from src.utils.check_public_holiday import check_public_holiday

# %%

def main():
    today_date = datetime.today()
    day_of_week = today_date.weekday()
    time_in_hour = today_date.time().hour
    bus_list = None

    # Step 1: Check if today is after 2am and before 5am on a non-PH. (Not interested in buses that operates within these hours)
    # For PH, bus services that operates between 2-5am follows Eve of PH timings, which is what we are interested in. 
    (is_ph, is_eve_ph) = check_public_holiday(today_date)

    if not is_ph and time_in_hour in range(2,6):
        return None

    else:
        # Step 2: If the time now is between 12 - 5am, bus timings follows previous day
        if time_in_hour in range(0, 6):
            day_of_week = day_of_week - 1

            if day_of_week == -1: # Handle case where day of week = 0 (Mondays), where it is converted to 6 (Sundays)
                day_of_week = 6

        # Step 3: Allocate respective bus list
        if (is_ph or day_of_week == 6): 
            # Check if today is PH or Sunday
            bus_list = SUNDAY_PH_BUS
        elif day_of_week == 5:
            # Check if today is Saturday
            bus_list = SAT_BUS
        else:
            bus_list = WEEKDAY_BUS

        # Step 4: Query bus information and upload to directus!
        print(f'\n============ Retrieving information at bus stops ====================\n')
        bus_ph_dict_list = [get_bus_information(bus_stop_code, service_no) for bus_stop_code, service_no in bus_list["bus_stop"]]
        bus_ph_dict_list_cleaned = [bus for bus in bus_ph_dict_list if bus != {}]
        # Upload to directus if there are data
        if len(bus_ph_dict_list_cleaned) > 0:
            upload_to_directus(bus_ph_dict_list_cleaned, "buses")


    # Step 5: Check if current time is after 11pm on the eve of PH, or between 12am to 5am on a PH
    # This is the period when there are extension of bus services
    # This is not mutually exclusive to the normal collection of bus data
    if (is_eve_ph and time_in_hour == 23) or (is_ph and time_in_hour in range(0,6)):
        print(f'\n============ Today is eve of PH! Retrieving information at bus stops ====================\n')
        bus_ph_dict_list = [get_bus_information(bus_stop_code, service_no) for bus_stop_code, service_no in PH_EVE_BUS["bus_stop"]]
        bus_ph_dict_list_cleaned = [bus for bus in bus_ph_dict_list if bus != {}]
        # Upload to directus if there are data
        if len(bus_ph_dict_list_cleaned) > 0:
            upload_to_directus(bus_ph_dict_list_cleaned, "bus_eves")
        
    print(f'\n\n============ Above retrieved at {datetime.now(ZoneInfo("Singapore")).strftime("%Y-%m-%d %H:%M:%S")} ====================\n\n')

if __name__ == "__main__":
    main()



# %%



