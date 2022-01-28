sent = input().upper().split()
print(len(sent))


# 시행착오 -> set(sent)해서 같은 단어는 한번만 세어야 하는 줄 알고 뻘짓함. 
# 처음에 시간초과 나옴..