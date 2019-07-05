print  'One'
file_obj = open('test.txt', 'r')
print type(file_obj)
print file_obj.read()

print  'Two'
file_obj = open('test.txt', 'r')
# while(file_obj)
print file_obj.readline()

print  'Three'
file_obj = open('test.txt')
for line in file_obj:
    print line.strip()
print '\n'
#  strip trim '\n'

print  'Four'
file_obj = open('test.txt')
data_list = list(file_obj)
for line in data_list: print line.strip()
print '\n'

print  'Five'
file_obj = open('test.txt')
data_list = file_obj.readlines()
for line in data_list: print line.strip()
print '\n'

print 'Test'
f = open('test.txt', 'r')
print " ".join(f.readlines()[3:6])
print'\n'

print 'Close'
file_obj = open('test.txt')
file_obj.close()
# file_obj.read()

print 'Different coder'
file_obj = open('example_koi_8.txt')
print file_obj.read()

print "Codecs"
import codecs




