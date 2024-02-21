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
tel_list = []

for _, text in enumerate(texts):
    if text[0] not in tel_list:
        tel_list.append(text[0])
    if text[1] not in tel_list:
        tel_list.append(text[1])

for _, call in enumerate(calls):
    if call[0] not in tel_list:
        tel_list.append(call[0])
    if call[1] not in tel_list:
        tel_list.append(call[1])

print(f"There are {len(tel_list)} different telephone numbers in the records.")