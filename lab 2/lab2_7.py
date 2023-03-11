with open("example.txt",'r') as file1:
    content = file1.read()

content = content.replace("\n","")

with open("example.txt",'w') as file2:
    file2.write(content)
