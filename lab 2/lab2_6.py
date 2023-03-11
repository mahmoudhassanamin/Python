with open("example.txt","r") as file:
    fileList = file.readlines()
    fileList.reverse()
    for i in fileList:
        print(i)