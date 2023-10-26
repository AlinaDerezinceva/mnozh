a = [int(s) for s in input().split()]
b = set()
for c in a:
    if c in b:
        print('yes')
    else:
        print('no')
        b.add(c)