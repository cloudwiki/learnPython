'''
Find the send for the given email
'''

import fileinput, re

pattern = re.compile('From:\s+([a-zA-Z0-9_\- ]+)<[\w\-_]+@[\w]+\.[a-zA-Z]+>');

for line in fileinput.input():
    #print fileinput.filename()
    #print fileinput.filelineno(), line
    m = pattern.match(line)
    if m:
        print repr(fileinput.filelineno()) +"@" + fileinput.filename(), m.group(1)
    

