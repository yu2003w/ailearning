"""
class code examples with python
"""

#
# In python, class object is different from instance object
#
class Hello():
    # class variable
    description = "first class written with python"
    def __init__(self, msg):
        self.msg = msg

    def get(self):
        return self.msg
    
def thello():
    h = Hello("First python class")
    print(h.get())
    # class variables are shared by all instances of class objects
    print(h.description)
    print(Hello.description)
    # class attributes DO NOT need to be declared, they spring into existence 
    # # when they're assigned value firstly
    h.counter = 25
    while h.counter > 5:
        print(h.counter - 5)
        h.counter -=5
        
    del h.counter

def tscope():
    def do_local():
        spam = "local spam"

    def do_non_local():
        nonlocal spam
        spam = "non local spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After do_local", spam)
    do_non_local()
    print("After do_non_local", spam)
    do_global()
    print("After do_global", spam)

  

if __name__ == '__main__':
    tscope()
    print("global scope", spam) 
    thello()