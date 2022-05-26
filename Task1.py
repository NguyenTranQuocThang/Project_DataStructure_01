"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from enum import unique

from matplotlib import units
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
first_calls, second_calls, time_calls, durations = zip(*calls)
first_texts, second_texts, time_texts = zip(*texts)

merge_phones = first_calls+second_calls+first_texts+second_texts
unique_phones = set(merge_phones)

print("There are {} different telephone numbers in the records.".format(
    len(unique_phones)))


