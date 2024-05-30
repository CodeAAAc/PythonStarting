def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if month <=12 and year <=2024:
        if month > 7:
            month -= 1
        if month % 2 != 0:
            return 31
        else:
            if month == 2:
                if is_year_leap(year):
                    return 29
                else:
                    return 28
            return 30

print(days_in_month(2024, 23))
