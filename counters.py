"""
counters are the awesome tool
counters gives the taste of sql like add item , remove iterm , common among two items , count of each item etc
counter creates a dict of values from given list and generates count for the keys in list
this is basic functionality of counter
apart from that , it can add/subtract two list and perform operations on top of them
"""
from collections import  Counter
state1=["jio","jio","airtel","airtel","voda","bsnl"] #top teles in district
state2=["jio","airtel","airtel","voda","voda","bsnl","bsnl"]
#lets perform some analytics on list level
t1 = Counter(state1)
t2=Counter(state2)
print(t1)
print(t1.most_common(1))#gives alpha order when same value is there
print(t2)
print(t2.most_common(1))
clubbed = t1
clubbed.update(t2)
print(clubbed)
print(clubbed.most_common(2))
print(clubbed.subtract(t2))
print(clubbed)
print("common among two states",t1&t2)
