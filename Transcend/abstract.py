"""Implementing an Abstract Class"""


import abc

class MyBook(object):
    __metaclass__ = abc.ABCMeta

    def set_val(self,title):
        """set a value"""
        return

    def get_val(self):
        """get """
        return


class MyClass(MyBook):

    def set_val(self, title):
        self.val = title

    def get_val(self):
        return self.val

x = MyClass()
print(x.set_val("Sathi"))
print(x.get_val())

