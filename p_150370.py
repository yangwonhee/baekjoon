def solution(today, terms, privacies):
    answer = []
    t_year, t_month, t_date = map(int, today.split("."))
    term = {}
    for item in terms:
        k, v = item.split()
        v = int(v)
        term[k] = v
    for cnt, privacy in enumerate(privacies):
        cnt += 1
            
        pri_day, pri_term = map(str, privacy.split())
        p_year, p_month, p_date = map(int,pri_day.split("."))
        p_month += term[pri_term]
        
        if p_month > 12:
            # print(p_year, p_month)
            p_year = p_year + (p_month // 12) 
            p_month = p_month % 12
            # print(p_year, p_month)
            
        
        
        if t_year > p_year:
            answer.append(cnt)
        elif t_year == p_year and t_month > p_month:
            answer.append(cnt)
        elif t_year == p_year and t_month == p_month and t_date >= p_date:
            answer.append(cnt)
        else:
            continue
    return answer