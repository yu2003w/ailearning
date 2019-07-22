import basic.contrl as ctl
import basic.operator as op
import basic.tclass as cls

def test():
    op.arithmetic("basic arithmetic")
    ctl.trange()
    ctl.tfor()
    obj = cls.Hello()
    obj.hello("first class in python")

if __name__ == "__main__":
    print("Start to run vault programs.")
    test()
