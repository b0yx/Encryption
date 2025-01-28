EncryptedMessage = 'nkdolg'

Symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-+=[]{}|\\;:\'",.<>?/`~ '

for key in range(len(Symbols)):
    translatedMessage = ''
    for symbol in EncryptedMessage:
        if symbol in Symbols:
            symbolIndex = Symbols.find(symbol)
            translatedIndex = (symbolIndex - key) % len(Symbols)
            translatedMessage += Symbols[translatedIndex]
        else:
            translatedMessage += symbol
            
        print(f"The key = {key} , Text is : {translatedMessage}")

              

