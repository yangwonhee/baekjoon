n = int(input())

for i in range(n):
    data = input().split(' ')
    reverse = ' '.join(data[::-1])
    print(f"Case #{i+1}: {reverse}")