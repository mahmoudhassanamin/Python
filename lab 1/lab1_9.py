def evenNumbers(li):
    evenNumbersList = list()
    for value in li :
        if value%2 == 0:
           evenNumbersList.append(value)
    return evenNumbersList
 
length=int(input("Enter length of your list\n"))
li = list()
i = 0 

while i < length:
    li.append(int(input(f'Enter num{i+1} : ')))
    i+=1
    
print(evenNumbers(li))    
