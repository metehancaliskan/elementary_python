"""
 This function takes a integer value and if the value is even, divide by 2 (floor division) or if the
value is odd, calculate 3 * n + 1. The function print each value and
continue updating the value until it becomes 1.
 Parameters:n
 parameters type:integer
 return:
 Display hailstone series
 """
def hailstone(n):
    while n>1:
        print(n,end=' ')
        if (n%2==0):
            n=n//2
        else:
            n=3*n+1
    while(n==1):
        return n
for i in range(5,11):
    print(hailstone(i))