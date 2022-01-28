"""BHAVDEEP DHADUK -20CE024
Practical 3: Find Captain Room Number"""

from collections import Counter

print("Name :- Bhavdeep Dhaduk\nRollno :- 20CE024")
n = int(input())

list1 = list(map(int,input().split()))

dic1 = dict(Counter(list1))

for k,v in dic1.items():
    if(v==1):
        print(k)