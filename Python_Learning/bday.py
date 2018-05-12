"""Birthday app."""
import datetime


def print_header():
    """Print the header."""
    print('-------------------------------------')
    print('           BIRTHDAY APP')
    print('-------------------------------------')
    print()


def get_birthday_from_user():
    """Get information from the user."""
    print('When where you born? ')
    day = int(input("Day [DD]: "))
    month = int(input("Month [MM]: "))
    year = int(input("Year [YYYY]: "))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    """Calculate the time between dates."""
    this_year = datetime.date(
        target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    """Print information."""
    if days < 0:
        print("You had your birthday {} days ago this year.".format(-days))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("Happy birthday!!!")


def main():
    """Execute main method."""
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)


main()
