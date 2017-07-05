
class Parent(object):
    def __init__(self,value):
        self.value = value

    def spam(self):
        print('Parent.Spam', self.value)

    def grok(self):
        print('Parent.Grok')
        self.spam()