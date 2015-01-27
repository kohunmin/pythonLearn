#tabto4.py
__author__ = 'Administrator'

import re
import sys

def usage():
    print("Usage: python %s filename" % sys.argv[0])

try: f = open(sys.argv[1])
except: usage(); sys.exit(2)

msg = f.read()
f.close()
p = re.compile('ab')
changed = p.sub("c"*4, msg)

f = open(sys.argv[1], 'w')
f.write(changed)
f.close()