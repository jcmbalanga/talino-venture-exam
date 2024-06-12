def valid_parenthesis(data):
    open = ["{", "[", "("]
    pairs = {"}" : "{", "]" : "[", ")" : "("}
    last_open_symbols = []
    for i in data:
        if i in open:
            last_open_symbols.append(i)
        elif last_open_symbols[-1] == pairs[i]:
            last_open_symbols.pop()
        else:
            return False
    return True

print(valid_parenthesis("{}[]()"))
print(valid_parenthesis("([)]"))
print(valid_parenthesis("([]){}"))
print(valid_parenthesis("{[()]}"))
print(valid_parenthesis("[(((())))]"))
