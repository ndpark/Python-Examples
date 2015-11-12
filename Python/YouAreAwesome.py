from sys import argv

script, filename = argv

print "This program is going to read %r and repalce its contents with \"You are awesome\" " %filename

txt = open(filename, 'w')

print "Now it will erase everything"

txt.truncate()
print "Everything is now replaced with \"You are awesome\" "
Awesome = ("You are awesome " + "\n") *99  
txt.write(Awesome * 99)