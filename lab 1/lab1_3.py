
def maximum1(li):
    li.sort()
    return li[length-1]
# refactor
def maximum2(li):
    return max(li)
length=int(input("Enter length of your list\n"))
li = list()
i = 0 

while i < length:
    li.append(int(input(f'Enter num{i+1} : ')))
    i+=1

print(maximum1(li))
print(maximum2(li))
