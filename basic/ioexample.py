# basic demo for input/output example
import math
import json

def tstring():
    print(f'value of PI is about {math.pi: .6f}')
    tdict = {"jacky": 4597, "tommy": 9876, "joe": 8876}
    for k, v in tdict.items():
        print(f'{k:10} ==> {v:10}')
    animals = 'eels'
    print(f'My hovercraft is full of {animals}.')
    print(f'My hovercraft is full of {animals!r}.')
    
    # str.format usage
    print('we are {} who say "{}!"'.format("knights", "Ni"))
    print("{1} and {0}".format("spam", "eggs"))
    print("{0} and {1}".format("spam", "eggs"))

    print("this {food} is {adjective}".format(food="spam", adjective="horrible"))
    print("{1} and {0} are both my {adjective}".format("eggs", "spam", adjective="favorites"))

    print("Jacky: {0[jacky]:d}, Tom: {0[tommy]:d}, Joe: {0[joe]:d}".format(tdict))
    print("Jacky: {jacky:d}, Tom: {tommy:d}, Joe: {joe:d}".format(**tdict))

def tfile():
    print("demo basic usage for file operation")
    with open("in.txt", "w+") as f:
        f.write("5\n")
        f.write(str(list(range(45, 60, 3))))
    with open("in.txt", "r") as f:
        data = f.read()
        print(data)
        f.seek(0)
        con = f.readline()
        while con != '':
            con = con.rstrip()
            print(con)
            con = f.readline()
        f.seek(0)
        for line in f:
            print(line.rstrip())
    
def tjson():
    print("read/writing json into file")
    with open("./js.txt", "w+") as f:
        teldict = {"jacky": 4298, "jared": 5027, "sam": 3289}
        json.dump(teldict, f)
    
    with open("./js.txt", "r") as f:
        print(json.load(f))

if __name__ == "__main__":
    tstring()
    tfile()
    tjson()
