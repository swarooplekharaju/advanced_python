"""
default dict helps us in shortening the dict value assignments
some times the dict[new_key]=value can genrate initialization errors
"""
#case 1

group1=["jio","jio","airtel","airtel","voda"]
#now i would like to store each value and cal its count
#lets try with normal dict
d={}
"""
for i in group1:
    if i in group1:
        d[i]+=1
print(d)

the above code generates error because when a dicts key is defined we need to atleast initialize its value
because python is a duck typed language 
hence instaed of again checking the d.keys() and assiging and a work around we go for fefault dict
"""
from collections import  defaultdict
d =defaultdict(int)
for i in group1:
    if i in group1:
        d[i]+=1
print(d)
print(d.keys(),d.values())
# this is the beauty of default dict
#identify the type for the given dict
#close the issues with default dict
