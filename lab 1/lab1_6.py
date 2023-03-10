def checkOnSign(num):
    if num > 0:
        return "positive"
    elif num == 0:
        return "Zero"
    else:
        return "negative"

x = int(input("Enter your number to check on its sign : "))
print(checkOnSign(x))