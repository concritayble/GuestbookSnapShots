#!/usr/bin/python

# Open a file
fo = open('/users/cosmigitana/Desktop/foo.txt','rw+')
print ("Name of the file: ", fo.name)

line = fo.readline()
print ("Read Line: %s" % (line))

# Again set the pointer to the beginning
#knowing that x refers to the position on the line and y to the line number
fo.seek(0, 0)
line = fo.readline()
print ("Read Line: %s" % (line))

# Close opend file
fo.close()