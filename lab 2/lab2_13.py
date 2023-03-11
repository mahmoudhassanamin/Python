def maxMinNumbers (li):
    if isinstance(li,list):
        return {"maxNumber":max(li),"minNumber":min(li)}
try:  
    li =list() 

    length = int(input("How many your elements ? "))

    for i in range(0,length):
        li.append(int(input(f'enter number {i+1} : ')))
        
    print(maxMinNumbers(li))
except:
    print("The inputs must be numbers")
