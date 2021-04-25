# the solution of part a
for i in range(1,11):
    a=pow(2,i)
    print('2 to the power {} is {}'.format(i,a))

# the solution of part b
x=0
y=0
while(y<5000):
    y=pow(2,x)
    x+=1
print('First power of 2 > 5000 is 2 to the power {} which is {}'.format(x-1,y))