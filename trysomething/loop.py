

LL = [1, 2, 3, 4, 5]
DL = {1: '1', 2: '2', 3: '3', 4: '4'}


def Try0():
    for l in LL: print(l)

def Try1():
  return any(l in [4, 6] for l in LL)



def Try2():
    gen = (l for l in LL  if not l%2)
    for l in gen:
        print(l)


def Try3():
    for x in filter(lambda w: w in LL, DL):
        print(x)

Try0()
print(Try1())
Try2()
Try3()