def test(a):
    a[0]=5

def test2(a):
	a["ha"]=6

b=list()
b.append(2)
print "b=%d" %b[0]

test(b)

print "b=%d" %b[0]



c={"ha" : 0}
print "c=%d" %c["ha"]

test2(c)

print "c=%d" %c["ha"]

