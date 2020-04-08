# Elizabeth Fuller
# 4/7/2020
# Palindrome Check modification

def check(string):
    length = len(string)
    if length == 1 or length == 0:
        return True
    else:
        if string[0] == " ":
            string = string.replace(string[0],'')
        if string[-1] == " ":
            string = string.replace(string[-1],'')
        if string[0] != string[-1]:
            return False
        else:
            check(string)


def prepare(string):
    string = string.strip()
    string = string.lower()
    newString = ""
    if not string.isalpha():
        for char in string:
            newString += char
    pali = check(newString)
    return pali

print("Enter string to check for palindrome:")
userString = input("> ")
pali = check(userString)
print(pali)
