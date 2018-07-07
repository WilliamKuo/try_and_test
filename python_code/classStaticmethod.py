class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_test(cls):
        print "test"

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)
        #cls.class_test()
        #cls.static_foo(x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x    


print "="*60

print "a=A()"
a=A()

print "="*60

print "a.foo(1)"
print a.foo(1)
#print "A.foo(1)"
#print A.foo(1)


print "="*60

print "a.class_foo(1)"
print a.class_foo(1)
print "A.class_foo(1)"
print A.class_foo(1)

print "="*60
print "a.static_foo(1)"
print a.static_foo(1)
print "A.static_foo(1)"
print A.static_foo(1)


print "="*60






