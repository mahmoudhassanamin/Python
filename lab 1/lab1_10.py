# algorithm 1
def sortString1(string):
    if isinstance(string,str):
        string=list(string)
        stringLength = len(string)
        i = 0
        j = 0
        while i < stringLength-1:
            j+=i+1
            while j < stringLength:
                if str.upper(string[i]) > str.upper(string[j]) :
                    temp=string[j]
                    string[j]=string[i]
                    string[i]=temp
                j+=1
            i+=1
            j = 0
        return string
    else:
        print("input must be string")
    
# algorithm 2
def sortString2(string):
    if isinstance(string,str):
        string=list(string)
        string.sort()
        return string
    else:
        print("input must be string")
    

string = input("Enter your string \n")
# algorithm 1
print(sortString1(string))

#algorithm 2
# print(sortString2(string))