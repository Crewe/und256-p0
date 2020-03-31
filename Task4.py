"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def getAllKnownCallers():
    """
    Returns a set of all numbers that have made an outbound call.
    """
    callers = set()
    for caller in calls:
        callers.add(caller[0])
    return callers


def getAllKnownCallees():
    """
    Returns a set of all numbers that have received an inbound call.
    """
    callees = set()
    for callee in calls:
        callees.add(callee[1])
    return callees


def getAllKnownTexters():
    """
    Returns a set of all numbers that have sent a text message.
    """
    texters = set()
    for texter in texts:
        texters.add(texter[0])
    return texters


def getAllKnownTextees():
    """
    Returns a set of all numbers that have received a text message.
    """
    textees = set()
    for textee in texts:
        textees.add(textee[1])
    return textees


def getKnownTelemarketers():
    """
    Returns a list of know telemarketers. Calls made from area code '140'.
    """
    telemarketers = set()
    # Get known telemarketer numbers. They start with "140"
    for tm in calls:
        if tm[0][:3] == "140":
            telemarketers.add(tm[0])

    # See if telemarketer numbers receive any calls. If they
    # do remove them from the list.
    for tm in calls:
        if tm[1][:3] == "140":
            telemarketers.remove(tm[1])

    return telemarketers


def getTelemarketers():
    """
    Returns a list of numbers that are potential, and known telemarketers.
    Numbers that have not received a call or text, or have not sent a text.
    """
    callers = getAllKnownCallers()
    callees = getAllKnownCallees()
    texters = getAllKnownTexters()
    textees = getAllKnownTextees()
    telemarketers = getKnownTelemarketers()

    # Remove known telemarketers from list
    t = set(callers).difference(telemarketers)
    # Remove known numbers that have received calls
    t.difference_update(callees)
    # Remove those who have sent a text
    t.difference_update(texters)
    # Remove those who have received a text
    t.difference_update(textees)
    # Join with known telemarketers
    t = set(telemarketers).union(t)

    return sorted(t)


def main():
    """
    Main program.
    """
    print("These numbers could be telemarketers: ")
    for telem in getTelemarketers():
        print(telem)


if __name__ == "__main__":
    main()