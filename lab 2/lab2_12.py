def swapKeyValue (dictionary):
    if isinstance(dictionary,dict):
        newDict={}
        for k,v in dictionary.items():
            newDict[v]=k
        return newDict
    

try:
    dictionary={} 

    length = int(input("How many your elements ? "))

    for i in range(0,length):
        dictionary.update({input(f'enter the Key {i+1} : '):input(f'enter the value {i+1} : ')})

    newDict = swapKeyValue(dictionary)
    print(newDict)
except:
    print("the length must be number")



