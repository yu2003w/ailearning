# basic string operations

def strop(tname):
    if tname is None:
        print("""\
        Usage: strop(tname)
               Please specify test name to run string operations
        """)
        return
    print(tname)
    basicop()
    builtinop()

def basicop():
    print("demo basic string operations")
    sstr = 'hello world, "how are u?'
    print(sstr)
    dstr = "who's there"
    print(dstr)
    ssstr = 'single \' in string'
    print(ssstr)
    ddstr = "double \" in string"
    print(ddstr)
    vstr = 3*'un' + 'ium'
    print(vstr)
    mstr = ('text could be splitted into multiple lines'
            'only works for text, variables and expressions are not supported')
    print(mstr)

    indstr = 'hello python'
    print(indstr[0] + indstr[-1])
    print(indstr[-8:-2])
    print(indstr[-9:55])
    print(indstr[:-2])
    print(indstr[-6:])
    print('string length is', str(len(indstr)))
    
def builtinop():
    print("demo builtin str operations")
    # construct with raw string
    spath = str(r'c:\some\time')
    print(spath)

if __name__ == "__main__":
    strop(None)
    strop("demo string operations")
