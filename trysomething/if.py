


def ifreturn(b):
    s = 0
    s = 5 if b else s
    print(s)

def ifdo(b):
    print(0) if b else print(5)

if __name__=='__main__':
    ifreturn(False)
    ifdo(False)