
my_set = {'a', 'b', 'c', 'c', 'c', 'c'}
print(my_set)

my_set.add('d')
print(my_set)

# contant-time lookups
large_set = set()
for i in range(10_000_000):
    large_set.add(i)

import time
start = time.time()
print(9_999_999 in large_set)
print(f'{time.time() - start}s elapsed')