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

total_call_time = {}

for _, call in enumerate(calls):
    if call[2][6:10] == '2016' and call[2][:2] == '09': 
        if call[0] not in total_call_time.keys():
            total_call_time[call[0]] = int(call[3])
        else:
            total_call_time[call[0]] += int(call[3])
        if call[1] not in total_call_time.keys():
            total_call_time[call[1]] = int(call[3])
        else:
            total_call_time[call[1]] += int(call[3])


max_num = ''
max_time = 0
for key in total_call_time.keys():
    if total_call_time[key] > max_time:
        max_time = total_call_time[key]
        max_num = key


print(f"{max_num} spent the longest time, {max_time} seconds, on the phone during September 2016.")