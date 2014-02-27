#!/usr/bin/env python

# write a text file
f = open("TestConfig.txt", "r+")
f = open('/users/cosmigitana/Desktop/TestConfig.txt','r+')

firstread = f.readlines()   
 # Take a snapshot of initial file
 
f.seek(0,0)    
# Go back to beginning and search for line in f:
if line.find('1'):
                print 'line matched'
                f.seek(1,1)       
                # Move one space along
f.write('house\n')     
                # f.write overwrites the exact number of bytes.
#break                    
                # leave loop once '1' is found

f.close()








