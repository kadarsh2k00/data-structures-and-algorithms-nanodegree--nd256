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


outgoing_calls = []
incoming_calls = []
outgoing_texts = []
incoming_texts = []

for i in range(len(calls)):
     outgoing_calls.append(calls[i][0])
     incoming_calls.append(calls[i][1])

for i in range(len(texts)):
    outgoing_texts.append(texts[i][0])
    incoming_texts.append(texts[i][1])
    
telemarketers = []
for num in set(outgoing_calls):
     if(num not in set(incoming_calls) and num not in set(outgoing_texts) and num not in set(incoming_texts)):
         telemarketers.append(num)

print("These numbers could be telemarketers: ")
for num in sorted(telemarketers):
     print(num)






























