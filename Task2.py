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
def sumCallLengths():
    """
    Returns a dictionary of phone numbers with the time they have spent
    on the phone in seconds.
    """
    call_lengths = {}
    for call in calls:
        # Add or sum the call duration for an outgoing call
        try:
            call_lengths[call[0]] += int(call[3])
        except:
            call_lengths[call[0]] = int(call[3])
        # Add or sum the call duration for an incomming call
        try:
            call_lengths[call[1]] += int(call[3])
        except:
            call_lengths[call[1]] = int(call[3])
        
    return call_lengths


def longestCall(call_list):
    """
    Returns the phone number of caller with the longest call as well
    as the length of the call in seconds.
    """
    duration = 0
    number = ""
    for phone, dur in call_list.items():
        if dur > duration: 
            number = phone
            duration = dur

    return (number, duration)


def main():
    """
    Main program.
    """
    caller, length = longestCall(sumCallLengths())
    s = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(
        caller, length)
    print(s)


if __name__ == "__main__":
    main()