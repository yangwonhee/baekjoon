import sys
n = input()
data = []
for i in range(len(n)):
    data += n[i]
    data[i] = int(data[i])

data.sort(reverse=True)

result = "".join(map(str, data))
print(int(result))