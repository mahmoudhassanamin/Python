with open("example.txt",'r') as file1:
    content = file1.read()

with open("copy.txt",'w') as file2:
    file2.write(content)