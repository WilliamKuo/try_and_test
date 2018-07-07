

a = 5
b = '5'
try:
    print 'try'
    print a + b
    raise  

except Exception as e:
    print 'exception'
    print repr(e)
