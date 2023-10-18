stack = []

words = input()

before = []
after = []

for w in words:
    if w in ['[', '(']:
        before.append(1)
    else:
        after.append(1)
    
    if before and after:
        if len(before) < len(after):
            print(0)
            exit()

for word in words:
    if  word in ['(' , '[']:
        stack.append(word)
    else:
        if not stack:
            print(0)
            exit()
        if word == ')' and stack[-1] == '(':
            stack.pop()
            stack.append(2)
        elif word == ']' and stack[-1] == '[':
            stack.pop()
            stack.append(3)
        else:
            tmp = 0
            while stack:
                stack_word = stack.pop()
                if type(stack_word) is int:
                    tmp += stack_word

                if stack_word == '[' :
                    if word == ']':
                        tmp *= 3
                        stack.append(tmp)
                        break
                    else:
                        print(0)
                        exit()
                elif stack_word == '(' :
                    if word == ')':
                        tmp *= 2
                        stack.append(tmp)
                        break
                    else:
                        print(0)
                        exit()
            
try:
    print(sum(stack))
except:
    print(0)