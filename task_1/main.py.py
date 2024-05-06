from datetime import datetime

def get_days_from_today(date):
    # Exception handling. If the date format is entered correctly.
    try:
        # Converting a date string in the 'YYYY-MM-DD' format into a datetime object.
        date_object = datetime.strptime(date, '%Y-%m-%d')
        # Getting the current date using datetime.today().
        date_now = datetime.today()
        # Calculating the difference between the current date and the specified date.
        result = date_now - date_object
        # Returning the difference in days as an integer.
        return result.days
    # Exception handling. If the date format is entered incorrectly.
    except ValueError:
        return "Invalid date format. Please enter the date in 'YYYY-MM-DD' format."

print(get_days_from_today("2020-10-09")) 