def summtion (li):
    if isinstance(li,list):
        sum = 0 
        for i in range(0,len(li)):
            sum+=li[i]
        return sum
    else:
        print("please enter only numbers")

li =list() 

length = int(input("How many your elements ? "))

for i in range(0,length):
    li.append(int(input(f'enter number {i+1} : ')))

print(f'the summtion = {summtion(li)}')