## This code is assumed to be running on Wednesdays to check if tomorrow is the 1st and 3rd Thursday of the month
## When Monday is the start of the week, Thursday is the 3rd week day
from datetime import date, timedelta

today = date.today()

def date_checker():
    Thurs = today + timedelta(days=1)
    Thurs_Day = Thurs.day
    day_of_week_tmr = today + timedelta(days=1)
    if day_of_week_tmr.weekday == 3 and 1 <= Thurs_Day <= 7:
        print("This week contains the first Thursday of the month")
    elif day_of_week_tmr.weekday == 3 and 15 <= Thurs_Day <= 21:
        print("This week contains the third Thursday of the month")
    else:
        print("Don't need to do anything this week")
    return

if __name__ == '__main__':
    date_checker()
