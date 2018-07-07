def return_fun():
    a = 1
    b = 1
    return a
             
print return_fun()
print return_fun()
print "--------------------------"

def yield_fun():
    a = 1
    b = 1
    yield a
    yield b

print yield_fun()


print "--------------------------"


def yield_fun():
    a = 3
    b = 2
    yield a
    c = 4
    yield b
     
generator = yield_fun()
print generator.next()
print generator.next()

print "--------------------------"


def yield_fun():
    a = 3
    b = 2
     
    b = yield a
    yield b
     
 
generator = yield_fun()
print generator.next()
print generator.send(8)
















