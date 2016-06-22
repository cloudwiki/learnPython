import sys, fileinput, re, pprint, os

userdir = r'C:\Users\meng_\Documents\workspaces\python\file_test'
print
print "get all entries: "
pprint.pprint(os.listdir(userdir) )
all_entries = [(userdir + "\\" + f) for f in os.listdir(userdir)]

txt_pattern = re.compile("\.(txt|log|conf|csv)$", re.I)
all_text_file = [ f for f in all_entries if txt_pattern.search(f)]
print
print "get all text file: "
pprint.pprint(all_text_file)

print
print "get all text file content"
for line in fileinput.input(all_text_file):
    print fileinput.filename() + '@' + repr(fileinput.lineno()) + "\t" + line


print "*"*20 + "write to file" + "*"*20    
file_to_write = open(r'C:\Users\meng_\Documents\workspaces\python\file_test\file_write.txt', 'w')

try:
    num = [ repr(x) for x in range(10)] #0-9
    file_to_write.write(''.join(num))
    file_to_write.write("\n")
    az = map(chr, range(97,123))
    file_to_write.write(''.join(az))
    file_to_write.write("\n")
    az = map(chr, range(65,91))
    file_to_write.write(''.join(az))
    file_to_write.write("\n")
except Exception as e:
    print "fail to write to file\n", e
else:
    print "finish writing files"
finally:
    file_to_write.close()

print "*"*20 + "random access" + "*"*20

with open(r'C:\Users\meng_\Documents\workspaces\python\file_test\file_write.txt', 'r') as file_to_read:
    print "printing file content"
    pprint.pprint(file_to_read.readlines())
    
with open(r'C:\Users\meng_\Documents\workspaces\python\file_test\file_write.txt', 'r') as file_to_update:
    print "Current position: " + repr(file_to_update.tell())
    print "Read 5 bytes from current pos: " + file_to_update.read(5)
    print "Goto the 9th byte: "
    file_to_update.seek(8)
    print "Current position: " + repr(file_to_update.tell())
    print "Read 1 byte from 8th byte: " + file_to_update.read(1)
    print "Goto the 0 : "
    file_to_update.seek(0)
    print "Goto the second line : "
    file_to_update.seek(12)
    print "read every 2nd lower letter"
    for i in range(26):
        #print file_to_update.tell()
        file_to_update.seek(1, 1)
        print file_to_update.read(1)
