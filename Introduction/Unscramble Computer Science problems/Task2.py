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

def max_caller(max_duration):
     for key,value in total_duration.items():
          if value==max_duration:
               return '{} spent the longest time, {} seconds, on the phone during September 2016.'.format(key,value)

total_duration ={ }

for i in range(len(calls)):
     total_duration[calls[i][0]] = total_duration.get(calls[i][0],0) + int(calls[i][3])
     total_duration[calls[i][1]] = total_duration.get(calls[i][1],0) + int(calls[i][3])

max_duration = max(total_duration.values())

print(max_caller(max_duration))
