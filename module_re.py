import re, glob
p = re.compile('.*p.*n.*')
for i in glob.glob('*'):
    m = p.match(i)
    if m:
        print m.group()
