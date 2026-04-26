n = int(input())
edges = []
adj = [[] for _ in range(n)]

for i in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v))
    adj[u].append(i)
    adj[v].append(i)


special = -1
for i in range(n):
    if len(adj[i]) >= 3:
        special = i
        break

res = [-1] * (n - 1)
label = 0


if special != -1:
    for edge_idx in adj[special][:3]:
        res[edge_idx] = label
        label += 1


for i in range(n - 1):
    if res[i] == -1:
        res[i] = label
        label += 1

# Output
for x in res:
    print(x)
