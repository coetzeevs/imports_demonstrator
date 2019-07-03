from helpers import DemoClass, sum

try:
    print('Instantiate class object...')
    class_object = DemoClass(name='MyOwnName')
    print('Call object method...')
    obj_string = class_object.__str__()
    print(f'object string = {obj_string}')
except:
    raise

try:
    print('Get sum of values...')
    val = sum(a=1, b=2)
    print(f'sum of values = {val}')
except:
    raise
