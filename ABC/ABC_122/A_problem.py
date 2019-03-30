b = input()

at = ['A', 'T']
gc = ['G', 'C']

if b in at:
    at.remove(b)
    print(at[0])
else:
    gc.remove(b)
    print(gc[0])
