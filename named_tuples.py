"""
named tuples gives the opportunity to initialize and identify the memberes of the tuple

lets see
its not a direct ds , hence we need to import from
"""

from collections import  namedtuple

run_rate = namedtuple("run_rate",'name  avg')
run_rate1 = run_rate("sachin",93.2)
run_rate2 =run_rate("shewag",87.2)
print(run_rate)
print(run_rate1)
print(run_rate2)
print(run_rate1.name)
"""
lets suppose the saching scored even more in latest 3 matches and increased his rate
dont worry named tuples have replace function to do that  
"""

run_rate1 = run_rate1._replace(avg=94.1)
print(f'new top 1 is{run_rate1}' )
