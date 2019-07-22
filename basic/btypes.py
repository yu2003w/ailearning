"""
examples for lists, slices and so on
"""

def tlist(tname):
    print("testing " + tname)
    al = [1,3,5,7,9]
    print(al)
    al += [11, 13, 15]
    print("appended slices:\n", al)
    al.append("lists ended")
    al[7] = 16
    print(al)
    al1 = al[2:8]
    print(al1)
    al1[:] = []
    print("clear lists", al1)

if __name__ == '__main__':
    print("testing builtin types such as lists, slices and so on")
    tlist("lists")