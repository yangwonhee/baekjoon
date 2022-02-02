n, m = map(int, input().split())
sum = 0
card_list = list(map(int, input().split()))
t = len(card_list)

for i in range(0, t-2):
    for j in range(i+1, t-1):
        for k in range(j+1, t):
            if card_list[i] + card_list[j] + card_list[k] > m:
                continue
            else:
                sum = max(sum, card_list[i] + card_list[j] + card_list[k])

print(sum)