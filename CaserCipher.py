import pyperclip

message = input("Put your message: ")
key = int(input("Put the key: "))
mode = int(input("Choose the mode:\nEncrypt == 1 || Decrypt == 2 :\t"))

Symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-+=[]{}|\\;:\'",.<>?/`~ '

TranslatedMessage = ''

for symbol in message:
    if symbol in Symbols:
        SymbolIndex = Symbols.find(symbol)
        
        # Determine the new index based on the mode
        if mode == 1:  # Encryption
            EncryptIndex = (SymbolIndex + key) % len(Symbols)
        elif mode == 2:  # Decryption
            EncryptIndex = (SymbolIndex - key) % len(Symbols)
        
        TranslatedMessage += Symbols[EncryptIndex]
    else:
        # If the symbol isn't in the Symbols list, keep it as is
        TranslatedMessage += symbol

print("Translated Message:", TranslatedMessage)
pyperclip.copy(TranslatedMessage)
