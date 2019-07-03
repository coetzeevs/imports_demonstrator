"""
Class to demonstrate import errors
Simply has an __init__ method and a method to return a human readable string of text
"""

class DemoClass(object):

    def __init__(self, name=None):
        self.name = 'DemoClass' if name is None else name
        self.description = 'A demo class that does nothing'

    def __str__(self):
        """
        Return the objects name
        """
        return self.name

"""
Simple function that takes two int values and returns the sum
"""

def sum(a, b):
    return a + b
