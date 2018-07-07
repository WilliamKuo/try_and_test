import re

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    print s1
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

test = 'ZZZApplePieYYYYi'
print test
print convert(test)
