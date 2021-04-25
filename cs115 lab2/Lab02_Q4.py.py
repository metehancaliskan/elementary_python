# the solution that use a while loop that iterates through a range.
test_str=input('Enter a string:')
new_str=''
i=0
while i in range(len(test_str)):
    if (test_str[i].isalnum() or test_str[i].isspace()):
        new_str+=test_str[i]
    i+=1
print('New string:{}'.format(new_str))
# the solution that use a for loop that iterates through each character in the string.
new_str2=''
for a in test_str:
    if (a.isalnum() or a.isspace()):
        new_str2+=a
print('New string:{}'.format(new_str2))
# the solution that use a while loop that iterates through a range.