from src.config.public_holiday import PUBLIC_HOLIDAY
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

today_date = datetime.now(ZoneInfo("Singapore"))
def check_public_holiday(today_date = today_date):
    IS_PH = False
    IS_EVE_PH = False
    today_date_string = today_date.strftime("%Y-%m-%d")

    next_day_date = today_date + timedelta(days=1)
    next_day_date_string = next_day_date.strftime("%Y-%m-%d")

    today_year = today_date.year

    ph_list = PUBLIC_HOLIDAY.get(f"{today_year}", "NOT UPDATED")

    if ph_list == "NOT UPDATED":
        raise ValueError(f"PH_LIST for year {today_year} not updated!")
    else:
        for ph_date in ph_list:
            if today_date_string == ph_date:
                # Today is PH
                IS_PH = True
                break
            if next_day_date_string == ph_date:
                # Next day is PH = Today is PH eve
                IS_EVE_PH = True
                break
    return (IS_PH, IS_EVE_PH)

