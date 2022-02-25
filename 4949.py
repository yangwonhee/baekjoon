while True:
    data = input()
    if data == ".":
        break
    stack = []
    tf = True
    for i in data:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] == "[":
                tf =False
                break
            elif stack[-1] == "(":
                stack.pop()
        elif i == "]":
            if not stack or stack[-1] == "(":
                tf = False
                break
            elif stack[-1] == "[":
                stack.pop()
    if tf == True and not stack:
        print("yes")
    else:
        print("no")
            
