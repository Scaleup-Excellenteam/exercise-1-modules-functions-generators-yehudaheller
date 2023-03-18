from random import randrange
from datetime import datetime, timedelta


def get_random_date(start_date, end_date):
    # Calculate the total number of seconds between the two dates
    total_seconds = (end_date - start_date).total_seconds()

    # Generate a random number of seconds between 0 and the total number of seconds
    random_seconds = randrange(total_seconds)

    # Add the random number of seconds to the start date to get the new date
    new_date = start_date + timedelta(seconds=random_seconds)

    return new_date


import datetime


def get_start_date():
    while True:
        try:
            start_date_str = input("Enter the start date in the format YYYY-MM-DD: ")
            # Convert the input string to a datetime object to check for validity
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        except ValueError:
            print(f"Error: Invalid date, Please try again:")
        else:
            return start_date


def get_end_date():
    while True:
        try:
            end_date_str = input("Enter the end date in the format YYYY-MM-DD: ")
            # Convert the input string to a datetime object to check for validity
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            print(f"Error: Invalid date, Please try again:")
        else:
            return end_date


def main():
    # Accept input from the user
    start_date_str = get_start_date()
    end_date_str = get_end_date()

    # convert to string object from datetime object, and get the first element(date without time)
    start_date_str = str(start_date_str).split(' ')[0]
    end_date_str = str(end_date_str).split(' ')[0]

    # Convert the input strings to datetime objects
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

    # Generate a random date between the two input dates
    new_date = get_random_date(start_date, end_date)

    # Print the new date and check if it falls on a Monday
    if new_date.weekday() == 0:
        print("I have no vinaigrette!")
    print(new_date.strftime("%Y-%m-%d"))


if __name__ == '__main__':
    main()
