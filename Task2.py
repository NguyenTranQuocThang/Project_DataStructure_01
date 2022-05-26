"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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
first_calls, second_calls, time_calls, durations = zip(*calls)

combine_first_calls = list(zip(first_calls, durations))

combine_second_calls = list(zip(second_calls, durations))

duration_phones = {}

for i in combine_first_calls:
    duration_phones[i[0]] = int(duration_phones.get(i[0], 0)) + int(i[1])

for i in combine_second_calls:
    duration_phones[i[0]] = int(duration_phones.get(i[0], 0)) + int(i[1])

key = max(duration_phones, key=lambda k: duration_phones[k])

value = duration_phones[key]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(key, value))

# Big(O) = O(n) + O(n) + O(n) 
