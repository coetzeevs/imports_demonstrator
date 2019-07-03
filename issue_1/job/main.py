from ..helpers.demo_functions import DemoClass, sum

if __name__ == '__main__':
    try:
        class_object = DemoClas(name='MyOwnName')
        class_object.__str__()
    except:
        raise

    try:
        sum(a=1, b=2)
    except:
        raise
