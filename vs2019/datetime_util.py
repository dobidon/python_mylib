import datetime

def last_sunday(year, month):
    sundays = ""
    if (month > 0):
        if (month < 12):
            last_day_of_month = datetime.datetime(year=year, month=month+1, day=1)
        else:
            last_day_of_month = datetime.datetime(year=year + 1, month=1, day=1)

        loop_break = False

        while loop_break == False:
            last_day_of_month -= datetime.timedelta(days=1)
            if last_day_of_month.strftime("%w") == "0":
                sundays = "{}-{}-{}".format(year, month, last_day_of_month.strftime("%d"))
                # sundays = last_day_of_month.strftime("%d")
                loop_break = True

    return sundays

def year_sundays(year):

    ans = []
    for a in range(1,13):
        ans.append(last_sunday(year=year, month=a))

    return ans


if __name__ == '__main__':
    print("Last Sundays of Every Month Example - Year 2020:")
    print(year_sundays(2020))
