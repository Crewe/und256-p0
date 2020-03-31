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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def getBagaloreCalls():
  """
  Returns a list of numbers of Bangalore landlines that have made
  an outgoing call and the number they have called.
  """
  bangalore_calls = []
  # Is the nmubre a Bangalore landline?
  for call in calls:
    if call[0][:5] == "(080)":
      bangalore_calls.append((call[0], call[1]))
    
  return bangalore_calls

def areaCodesCalledByBangalorians():
  """
  Returns a list of the area codes of the numbers called by Bangalorian land lines.
  """
  numbers_called = set()

  for call in calls:
    # Is the number a Bangalore landline?
    if call[0][:5] == "(080)":
      # Bangalore number has called a mobile number
      if call[1].__contains__(" "):
        if call[1][0] == "7" or call[1][0] == "8" or call[1][0] == "9":
          numbers_called.add(call[1][:4])

  return sorted(numbers_called)


def bangToBangCallPercentage():
  """
  Returns the percentage of calls made from one Bangalore landline
  to another.
  """
  bangalore_calls = getBagaloreCalls()
  total_calls = len(bangalore_calls)
  bang_to_bang = 0.0
  for call in bangalore_calls:
    if call[1][:5] == "(080)":
      bang_to_bang += 1

  # Protect against divide by zero.
  if total_calls == 0:
    return "0%"
  else:
    return (bang_to_bang / total_calls) * 100.0


def main():
  """
  Main program.
  """
  print("The numbers called by people in Bangalore have codes:")
  for codes in areaCodesCalledByBangalorians():
    print(codes)
    continue

  print("{0:.0f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    bangToBangCallPercentage()))


if __name__ == "__main__":
    main()