def stringComparsion(li):
    return max(li)

length = int(input("Enter the length of your list : "))
li = list()
i =0 
while i < length:
    li.append(input(f'Enter string {i+1} : '))
    i+=1

print(stringComparsion(li))
