# func1 only runs when func2 finishes, func2 only runs when func3 finishes

def func3():
    print('Three')


def func2():
    func3()
    print('Two')


def func1():
    func2()
    print('One')


func1()
