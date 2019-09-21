# print syntax is different between python 3.x and 2.x

def trange():
    print('Simple range(2,5):')
    for i in range(2,5):
        print(i)
    print(repr(range(2,5)))
    
    for i in range(2, 10):
        for j in range(2,i):
            if i % j == 0:
                print(i, 'equals', j, '*', i//j)
                break
        else:
            print(i, 'is prime number')

    # specify increment for range
    for i in range(-10, -1, 3):
        if i % 2 == 0:
            print(i, "is even number")
            continue
        print(i, "is odd number")

def tfor():
    print("demo for loop usage")
    words = ["test", "for", "loop", "example"]
    for w in words:
        if w == "example":
            w = "examples"
        print(w, len(w))

    print(words)

    for i in range(len(words)):
        if words[i] == "example":
            words[i] = "examples"
            words.insert(i, "which")
    print(words)

    # another way to modify list is to iterate over slice
    for w in words[:]:
        if len(w) == 5:
            words.insert(0, w)
    print(words)

def mystery():
    """
    pass could be used for passing syntax checking
    """
    pass

def ask_ok(prompt, retries = 5, reminder = "Please try again"):
    """function with default values for arguments, a little interesting example"""
    if prompt is None or not prompt:
        print("missing prompt information")
        return
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'Y', 'YES'):
            return True
        if ok in ('n', 'no', 'N', 'NO'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError("invalid user input")
        print(reminder)

def task():
    ask_ok("")
    ask_ok(None)
    ask_ok("Do you confirm?")
    ask_ok("Do you confirm again?", 1)
    ask_ok("Do you confirm again and again?", 2, "try again")

def argval(a, L=[]):
    """
    Noted: default value only evaluated once and evaluated at the point 
    of function definition in the defining scope
    """
    L.append(a)

    return L

def tdefval():
    print(argval(1))
    print(argval(2))
    print(argval(3))

def cheeseshop(kind, *argv, **keywords):
    print("we are out of", kind)
    for arg in argv:
        print(arg)
    print("*" * 40)
    for kw in keywords:
        print(kw, keywords[kw])

def tvarparams():
    cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def tfib():
    print("testing fibonacci series")
    print(fib(10))

def fib(n):
    """reurns fibonacci series up to n"""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def dictparas(kind='knative', paas='k8s', bigdata='cdh', machinelearning='r'):
    print("demo unpacking argument list with **")
    print(paas, kind)

def unpackargs():
    print("demo unpacking argument lists")
    args = [3, 6]
    print(list(range(*args)))
    parad = {"kind":"knative", "paas":"mesos","bigdata":"hadoop","machinelearning":"anaconda"}
    dictparas(**parad)

def tlambda():
    print("demo lambda usage")
    f = calcu(2,4)
    print(f(1))
    
    f1 = calcu(5, 6)
    print(f1(2))

def calcu(a, b):
    return lambda x : x + a*b

if __name__ == "__main__":
    trange()
    tfor()
    tfib()
    task()
    tdefval()
    tvarparams()
    unpackargs()
    tlambda()
