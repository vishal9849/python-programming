import datetime


# 1 Day of the week
def get_week_day(usr_inp):
    days = {0: "Sunday", 1: "Monday", 2: 'Wednesday',
            3: 'Thursday', 4: "Friday", 5: 'Saturday',
            6: "sunday"}
    print("Day_of_the_week:", days.get(usr_inp.weekday()))


user_input = datetime.datetime.today()
get_week_day(user_input)


# 2 Return users age and time remaining in days, hours, min, seconds until next birthday
def birthday_data(user_year, user_month, user_day):
    current_date = datetime.datetime.now()
    future_birthdate = datetime.datetime(current_date.year + 1, user_month, user_day)
    print("Current_age", current_date.year - user_year)
    time_info = future_birthdate - current_date

    print("time__remaining_for_next_birthday", time_info)
    print("number_of_days_remaining:", time_info.days)
    print("number_of_hours_remaining:", (time_info.days * 24 + time_info.seconds) // 3600)
    print("number_of_minutes_remaining:", (time_info.seconds % 3600) // 60)
    print("number_of_seconds_remaining:", time_info.seconds % 60)
    print("number_of_micro_seconds_remaining:", time_info.microseconds)


year = 1996
month = 1
day = 28
birthday_data(year, month, day)


# 3 Total seconds of life
def total_number_of_seconds(user_year, user_month, user_day):
    birth_date = datetime.datetime(user_year, user_month, user_day)
    date_difference = datetime.datetime.now() - birth_date
    print("Total_number_of_seconds_lived:", date_difference.days * 24 * 3600)


year = 1996
month = 1
day = 28
total_number_of_seconds(year, month, day)


# 4 python program to print date for yesterday, today and tomorrow
def return_dates(inp):
    today = inp.date()
    yesterday = today + datetime.timedelta(days=-1)
    tomorrow = today + datetime.timedelta(days=1)
    print("yesterday", yesterday)
    print("today", today)
    print("tomorrow", tomorrow)


user_input = datetime.datetime.now()
return_dates(user_input)

