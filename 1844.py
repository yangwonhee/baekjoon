from collections import deque
def solution(maps):
    queue = deque()
    queue.append([[0, 0], 0])
    n = len(maps)
    m = len(maps[0])
    answer = n*m
    while queue:
        temp, index = queue.popleft()
        # print(temp, index)
        i, j = temp
        # if i < 0 or j < 0:
        #     print(i, j)
        if index > n*m:
            answer = -1
            break
        if maps[i][j] == 1:
            maps[i][j] = 0
            if i == n and j == m:
                if answer > index:
                    answer = index
            else:
                queue.append([[i+1, j], index+1])
                queue.append([[i, j+1], index+1])
                queue.append([[i, j-1], index+1])
                queue.append([[i-1, j], index+1])

    return answer


        
    
    
    