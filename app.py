print("please enter a word")
s = input()

tempString=""
for i in range (len(s)):
    if s[i]>='A' and s[i]<='Z':
        tempString+=chr(ord(s[i])+32)
    else:
        tempString+=chr(ord(s[i]))

isPal=True
for i in range(len(tempString)):
    l=len(tempString)-1
    if tempString[i]!=tempString[l-i]:
        isPal=False

formattedWord=""
for i in range(len(s)):
    if i==0:
        if s[i]>='a' and s[i]<='z':
            formattedWord+=chr(ord(s[i])-32)
        else:
            formattedWord+=s[i]
    else:
        if s[i]>='A' and s[i]<='Z':
            formattedWord+=chr(ord(s[i])+32)
        else:
            formattedWord+=s[i]

if isPal:
    print(formattedWord + " is a palindrome")
else:
    print(formattedWord + " is a not a palindrome")
