# code for basic arithmetic
import sys

"""
 try basic arithmetic operations
"""
def arithmetic(tname):
    if tname is None:
        print("""
        Usage: arithmetic(test name)
               Please specify test name to run arithmetic
        """)
        return
    print(tname)
    basic_op()
    com_op()

def basic_op():
    print ("basic arithmetic operations")
    val1 = 2 + 2
    val2 = 2 * 2
    val3 = val1 * val2
    val4 = val3 / val2
    print("val1 =",val1, ", val2 =", val2, ", val3 =", val3, ", val4 =", val4)
    # floor division with operator "//"
    val3 //= 3
    val4 %= 3
    print("val3 =", val3, ", val4 =", val4)
    val5 = val3 ** 5
    print("power calculation for", val3, "** 5 is", val5)

# TODO: add example for rational and complext
def com_op():
    print ("rational and complex operations")
    pass
    
    
if __name__ == "__main__":
    arithmetic(None)
    arithmetic("demo arithmetic operations")
