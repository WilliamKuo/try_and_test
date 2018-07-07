import itertools
my_list = [['11', '22', '33', '44'], ['33', '44', '55', '66']]
title = ['A', 'B', 'C', 'D']


for m in my_list:
    for k, v in itertools.izip(title, m): 
        print '{} {}'.format(k, v)




#foo = [1, 2, 3, 5, 7]
#bar = ['a', 'b', 'c', 'f', 'f']
#for f,b in itertools.izip(foo,bar):
#    print(f,b)
#for f,b in itertools.izip_longest(foo,bar):
#    print(f,b)
