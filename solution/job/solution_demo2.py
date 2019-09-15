from helpers import DemoClass, sum

def function1():
    try:
        print('Instantiate class object...')
        class_object = DemoClass(name='MyOwnName')
        print('Call object method...')
        obj_string = class_object.__str__()
        print(f'object string = {obj_string}')
    except:
        raise

    return None

def function2():
    try:
        print('Get sum of values...')
        val = sum(a=1, b=2)
        print(f'sum of values = {val}')
    except:
        raise

    return None

def main():
    # run function 1
    function1()

    # run function 2
    function2()

    return None
