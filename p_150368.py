def solution(users, emoticons):
    pcnt = []
    price = []
    cnt = 0
    for pc, pr in users:
        pcnt.append(pc)
        price.append(pr)
    pcnt = sorted(pcnt)[::-1]
    price = sorted(price)
    for min_pcnt in pcnt:
        money = 0
        for emo_pr in emoticons:
            money += emo_pr * min_pcnt * 0.01
            money = int(money)
        for min_pri in price:
            if min_pri <= money:
                cnt += 1
        print(cnt)
    
    
    answer = []
    
    return answer