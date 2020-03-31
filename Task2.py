"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import datetime
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def longestCall():
    """
    Returns the phone number of caller with the longest call as well
    as the length of the call in seconds.
    """
    duration = 0
    number = ""
    for call in calls:
        if int(call[3]) > duration: 
            number = call[0]
            duration = int(call[3])

    return (number, duration)


def main():
    """
    Main program.
    """
    caller, length = longestCall()
    s = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(
        caller, length)
    print(s)


if __name__ == "__main__":
    main()