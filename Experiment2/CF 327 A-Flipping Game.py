n = int(input())
arr = list(map(int, input().split()))

total_ones = sum(arr)

max_gain = 0
current = 0

for x in arr:
    val = 1 if x == 0 else -1
    current = max(val, current + val)
    max_gain = max(max_gain, current)

if max_gain == 0:
    print(n - 1)
else:
    print(total_ones + max_gain)
