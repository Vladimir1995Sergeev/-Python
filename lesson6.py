from itertools import count, cycle
my_count = count(1)
my_cycle = cycle("ABC")
for _ in range(8):
    print("({}={})".format(next(my_cycle), next(my_count)))