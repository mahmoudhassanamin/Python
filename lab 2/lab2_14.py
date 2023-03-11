def squares (li):
    if isinstance(li,list):
        i = 0 
        for elem in li:
            li[i]=elem**2
            i+=1
        return li 
try:
    li =list() 

    length = int(input("How many your elements ? "))

    for i in range(0,length):
        li.append(int(input(f'enter number {i+1} : ')))
        
    print(squares(li))

except:
    print("The inputs must be numbers")
