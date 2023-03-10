def numberOfVowels(string):
    counterOfVowels = 0
    for i in string:
        if i in vowels:
            counterOfVowels+=1
    return counterOfVowels

vowels = "aeiou"

string = input("Enter your String : ")
print(f'Number of vowels in your string = {numberOfVowels(string)}')
