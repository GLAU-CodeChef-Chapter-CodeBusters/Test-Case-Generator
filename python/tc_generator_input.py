import random

p = random.randint(1,1000) # number of test cases
x = str(p)+"\n"
for i in range(p):
    x += str(random.randint(-500,500)) # range of test case
    if(i!=p-1):
        x += "\n"
f = open('input009.txt','w')
f.write(x)
f.close()
