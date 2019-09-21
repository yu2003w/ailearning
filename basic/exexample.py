# basic usage for except example

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

def tclass():
    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print('D')
        except C:
            print('C')
        except B:
            print('B')

if __name__ == '__main__':
    tclass()