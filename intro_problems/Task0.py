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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

text_1 = texts[0]
call_1 = calls[0]

print(f"First record of texts, {text_1[0]} texts {text_1[1]} at time {text_1[2]}.")
print(f"Last record of calls, {call_1[0]} texts {call_1[1]} at time {call_1[2]}, lasting {call_1[3]} seconds.")
