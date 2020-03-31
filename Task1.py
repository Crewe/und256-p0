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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def uniquePhoneNumbers():
    """
    Returns the total number of unique phone numbers found in the logs.
    """
    unique_numbers = set()
    for call in calls:
        unique_numbers.add(call[0])
        unique_numbers.add(call[1])

    for text in texts:
        unique_numbers.add(text[0])
        unique_numbers.add(text[1])

    return len(unique_numbers)

def main():
    """
    Main program.
    """
    print("There are {} different telephone numbers in the records.".format(uniquePhoneNumbers()))


if __name__ == "__main__":
    main()