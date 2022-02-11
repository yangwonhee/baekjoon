import sys
from collections import Counter

N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline()))

sansul = round(sum(data)/N)
data.sort()
jungang = data[N // 2]

cnt = Counter(data).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    choibin = cnt[1][0]
else:
    choibin = cnt[0][0]

range = max(data) - min(data)

print(sansul)
print(jungang)
print(choibin)
print(range)