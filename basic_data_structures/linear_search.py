
def search(l: list, target: str) -> int:
    for index in range(0, len(l)):
        if l[index] == target:
            return index
    return -1

my_list = ['a'] * 100_000_000
my_list.append('b')

import time
start = time.time()
search(my_list, 'b')
end = time.time()

print(f'time elapsed = {(end - start)*1000:.2f}ms')