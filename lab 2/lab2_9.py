with open("example.txt","r") as file:
    content=file.read().split('\n')

print(max(content,key=len))

