
def exchange_items():
    L = [1,2,3,4,5,6]
    L[1], L[2] = L[2], L[1]
    print(L)

def slice_op():
    L = [1,2,3,4,5,6]
    l = L
    print(L[:2])
    l = l[:2] + [10] + l[2:]
    print(l)

# def list_unpack(l):
#     return *l

exchange_items()
slice_op()

# print(list_unpack([2]))
# print(list_unpack([2, 3]))
#
# def assert_list_unpack():
#     a, b = list_unpack([2, 3])
#     print(a)
#
# assert_list_unpack()


print(max([0,1,2]))

def reverse_usage(l):
    for i in reversed(l[:5]):
        print('*', i)


reverse_usage([1,2,3,4,5,6])