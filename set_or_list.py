"""
Extra Challenge: Set or list
You want to implement a code that will search for a number in a range.
You have a decision to make as to whether to store the number in a set
or a list. Your decision will be based on time. You have to pick a data
type that executes faster.
You have a range and you can either store it in a set or a list depending
on which one executes faster when you are searching for a number in
the range. See below:
a = range(10000000)
x = set(a)
y = list(a)
Let’s say you are looking for a number 9999999 in the range above.
Search for this number in the list and the set. Your challenge is to find
which code executes faster. You will pick the one that executes quicker,
lists, or sets. Run the two searches and time them.
"""

import time

a = range(10000000)
x = set(a)
y = list(a)

num = 9998899

start_time = time.time()
if num in x:
    print(f"{num} is in set")
end_time = time.time()
print(f"Time taken to search in set: {(end_time - start_time):.2f} seconds")

start_time = time.time()
if num in y:
    print(f"{num} is in list")
end_time = time.time()
print(f"Time taken to search in list: {(end_time - start_time):.2f} seconds")
