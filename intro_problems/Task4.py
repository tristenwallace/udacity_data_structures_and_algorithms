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

callers = set()
call_recievers = set()
texting_nums = set()

for sender, reciever, _ in texts:
    texting_nums.add(sender)
    texting_nums.add(reciever)

for caller, reciever, _, _ in calls:
    callers.add(caller)
    call_recievers.add(reciever)

possible_telemarkerters = callers - (texting_nums | call_recievers)

print("These numbers could be telemarketers: ")
for tel_number in sorted(possible_telemarkerters):
    print(tel_number)