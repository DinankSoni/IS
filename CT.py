def encrypt(text,s):
    result = ""
     # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
x = 1
while x > 0:
    num = int(input("what you need \n 1.Encrypted Message \n 2.Decrypted messagee \n 3.Cancle \n"))
    if num==1:
        text = input("Enter the text: ")
        key = int(input("Enter the key: "))
        print("Cipher: " + encrypt(text,key)+"\n")
    elif num==2:
        text = input("Enter the text: ")
        for i in range(1,26):
            key = i
            print("Plain text: " + encrypt(text,key)+"\n")
    elif num==3:
        break
    else:
        print("Enter correct number")