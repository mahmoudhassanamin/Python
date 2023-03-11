def sorting(listString):
   if isinstance(listString,list):
        li = list()
        for item in listString:
           if item[0] == "a" :
               li.append(item)
        return li

try:
    li =list() 

    length = int(input("How many your elements ? "))

    for i in range(0,length):
        li.append(input(f'enter string {i+1} : '))


    print(sorting(li))
except:
    print("the length must be number")
