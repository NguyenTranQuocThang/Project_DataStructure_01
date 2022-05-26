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
first_calls, second_calls, time_calls, durations = zip(*calls)
first_texts, second_texts, time_texts = zip(*texts)

merge_phones = set(second_calls+first_texts+second_texts)

phones = set(first_calls + second_calls+first_texts+second_texts)

marketing_phones = sorted(phones.difference(merge_phones))

print("These numbers could be telemarketers: ")

for i in marketing_phones:
    print(i)

# Big(O) = O(nlog(n))
