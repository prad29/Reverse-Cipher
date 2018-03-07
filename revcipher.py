import pyperclip


def encrypt():                                                        # This function takes the encrypted text and encrypts it by
                                                                      # reversing the order of the sequence
str=input("Enter Your Message\n")
    translated=''
    i=len(str)-1
    while i>=0:
        translated=translated+str[i]
        i-=1
    print("Encryption Complete :"+translated)

def decrypt():                                                      #This function takes in Encrypted text and returns the decrypted
                                                                    #text and returns it to the console
    str=input("Enter Encrypted Text\n")
    translated=''
    i = len(str) - 1
    while i >= 0:
        translated = translated + str[i]
        i -= 1
    print ("Decryption Complete :"+translated)


encrypt()
decrypt()
