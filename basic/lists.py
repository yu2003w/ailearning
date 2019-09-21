"""
examples for lists, slices and so on
"""
from collections import deque

def tlist(tname):
    print("testing " + tname)
    al = [1,3,5,7,9]
    for i, v in enumerate(al):
        print(i, v)
    for v in reversed(al):
        print(v)
    print(al)
    al += [11, 13, 15]
    print("appended slices:", al)
    al.append("lists ended")
    al[7] = 16
    print(al)
    al1 = al[2:8]
    print(al1)
    al1[:] = []
    print("clear lists", al1)
    # partially clear list
    al[4:7] = []
    print("partially clear list:", al)

def list_stacks():
    print("demo list as stacks")
    a1 = list(range(3,9))
    a1.append(10)
    print(a1)
    print("poped value", a1.pop())
    print(a1)

# using deque is efficient for both stack and queue
def list_queue():
    q1 = deque(["apple", "banana", "orange"])
    q1.append("pomelo")
    print(q1)
    print("poped value", q1.popleft())
    print(q1)

"""
list comprehensions
"""
def tlistcomprehension(tname):
    l1 = []
    # this loop will create/override variable x that still exists after loop completion
    for x in range(10):
        l1.append(x**2)
    print(l1)

    # this style will not generate variable named 'value' after loop completion
    numslice = [ value for value in range(1,21,2)]
    print(numslice)
    
    numslice = [ value**2 for value in range(3,31,3)]
    print(numslice)

    l2 = [(x, y) for x in [1, 2, 3] for y in [3, 2, 4] if x != y]
    print(l2)

    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(matrix1)
    matrix2 = [[row[i] for row in matrix1] for i in range(4)]
    print(matrix2)
    del matrix2[0]
    print(matrix2)
    del matrix2[1:2]
    print(matrix2)
    del matrix2
    # print(matrix2)

def ttuple():
    print("demo tuple usage")
    # tuple is immutable, however, it could contain mutable elements
    t = 12345, 6789, 'hello'
    print(t[0])
    print(t)
    u = (t, [1,2,3,4,5])
    print(u)
    # unpack tuple
    x, y, z = t
    print(x, y, z)

def tset():
    print("demo set usage")
    fruits = {"apple", "orange", "apple", "banana", "pomelo", "orange"}
    for f in sorted(fruits):
        print(f)
    print(fruits)
    # for empty set, set() should be used. '{}' will generate empty dict
    eset = set()
    print(eset)
    edict = {}
    print(edict)

def tdict():
    print("demo dictionary usage")
    teldict = {"jacky": 4298, "jared": 5027, "sam": 3289}
    for k,v in teldict.items():
        print(k, v)
    teldict["joe"] = 4097
    print(teldict)
    if "sam" in teldict:
        print(teldict["sam"])
        del teldict["sam"]
    print(teldict)
    dictc = { x: x**2 for x in range(2, 9, 3)}
    print(dictc)

if __name__ == '__main__':
    print("testing builtin types such as lists, slices and so on")
    tlist("lists")
    tlistcomprehension("slice")
    list_stacks()
    list_queue()
    ttuple()
    tset()
    tdict()
    