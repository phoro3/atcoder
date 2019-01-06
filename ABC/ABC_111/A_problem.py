N = input()
string = ['1' if c == '9' else '9' for c in N]
print(''.join(string))