from datetime import datetime, timedelta

date_format = "%Y-%m-%d"


def get_days_between_dates(start_date, end_date):
    start_dt = datetime.strptime(start_date, date_format)
    end_dt = datetime.strptime(end_date, date_format)
    delta = end_dt - start_dt

    day_list = list()
    for i in range(delta.days + 1):
        day = start_dt + timedelta(days=i)
        date = day.strftime(date_format)
        day_list.append(date)

    return day_list


def get_start_end_date_list(start_date, end_date):
    day_list = get_days_between_dates(start_date, end_date)
    start_date = day_list.pop(0)

    start_end_dates = list()
    for end_date in day_list:
        start_end_dates.append([start_date, end_date])
        start_date = end_date

    return start_end_dates


def get_start_end_last_month():
    end_dt = datetime.today()
    start_end_dates = list()

    for i in range(4):
        start_dt = end_dt - timedelta(days=7)
        start_date = start_dt.strftime(date_format)
        end_date = end_dt.strftime(date_format)
        start_end_dates.append([start_date, end_date])
        end_dt = start_dt

    return start_end_dates
