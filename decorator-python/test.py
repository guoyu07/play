#!/usr/bin/env python

class myDecorator(object):

    def __init__(self, f):
        print 'in myDecorator.__init__(self, f)'
        self.my_f = f
    def __call__(self):
        print 'outside of f 0'
        self.my_f()
        print 'outside of f 1'

@myDecorator
def func1():
    print 'in func1'

@myDecorator
def func2():
    print 'in func2'



func1()
func2()

