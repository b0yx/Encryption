import pyperclip

def main():
    Message = input("Put your message here :")
    Key = int(input("what is your key :"))
    
    CipherText = EncryptMessage(Key , Message)
    
    print(CipherText)
    
    pyperclip.copy(CipherText)
    
def EncryptMessage(Key , Message):
    CipherText = [''] * Key
    
    for column in range(Key):
        currectIndex = column
        while currectIndex < len(Message):
            CipherText[column] += Message[currectIndex]
            currectIndex += Key
    return ''.join(CipherText)


if __name__ == '__main__':
    main()

    

