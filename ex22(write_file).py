print "One"

fo = open('test.txt','w')
str1 = 'string for write\n'
fo.write(str1)
fo.close()

fo = open('test.txt','r')
print fo.read()

fo= open('test.txt', 'a')
str2 = 'second string\n'
fo.write(str2)
fo.close()

fo = open('test.txt','r')
print fo.read()

print "Two"

arr = range(1,11)
print arr

with open('test.txt','w') as fo:
    fo.writelines(i + "\n" for i in map(str, arr))