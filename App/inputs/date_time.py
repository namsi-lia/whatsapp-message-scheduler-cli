import datetime
import time

# Check time format
def check_time_format(send_time):
    is_valid = False
    try:
        datetime.datetime.strptime(send_time, "%H:%M")
    except ValueError as e:
        is_valid = False
    else:
        if datetime.datetime.strptime(send_time, "%H:%M"):
            is_valid = True
    return is_valid


# Check date format
def check_date_format(send_date):
    is_valid = False
    try:
        datetime.datetime.strptime(send_date, "%d/%m/%Y")
    except ValueError as e:
        is_valid = False
    else:
        if datetime.datetime.strptime(send_date, "%d/%m/%Y"):
            is_valid = True
    return is_valid

# get Today's Date
def get_todays_date():
    return datetime.date.today().strftime("%d/%m/%Y")

# get the time NOW
def get_time_now():
    return datetime.datetime.now().strftime("%H:%M")


# Check date given has not passed
def check_date_not_passed(today_date, send_date):
    today_date = datetime.datetime.strptime(today_date, "%d/%m/%Y")
    send_date = datetime.datetime.strptime(send_date, "%d/%m/%Y")
    if today_date <= send_date:
        return True
    else:
        return False


# Check time given has not passed
def check_date_time_not_passed(date_time_now, send_date_time):
    date_time_now = datetime.datetime.strptime(date_time_now, "%d/%m/%Y %H:%M")
    send_date_time = datetime.datetime.strptime(send_date_time, "%d/%m/%Y %H:%M")
    if date_time_now <= send_date_time:
        return True
    else:
        return False


# Countdown till message is sent
def countdown_timer(date_time_now, send_date_time):
    time_reached = False
    date_time_now = datetime.datetime.strptime(date_time_now, "%d/%m/%Y %H:%M")
    send_date_time = datetime.datetime.strptime(send_date_time, "%d/%m/%Y %H:%M")
    time_difference = send_date_time - date_time_now
    time_in_seconds = int(time_difference.total_seconds())
    while time_in_seconds:
        print(time_in_seconds, end="\r")
        time.sleep(1)
        time_in_seconds -= 1
    if time_in_seconds == 0:
        time_reached = True
    return time_reached
