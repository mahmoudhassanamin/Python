def swapKeyValue (**kwargs):
        newDict={}
        for k,v in kwargs.items():     
            newDict[v]=k
        return newDict

print(swapKeyValue(name="mahmoud",jop="engineer",age=28,phone=121))
