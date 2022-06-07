import sys
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'To be, or not to be, that is the question.'
    myKey = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    print('Original message: '+myMessage)
    print('Key: '+myKey+'\n\n')
    checkValidKey(myKey)
    translated = encryptMessage(myKey, myMessage)
    print('Encrypted Message: '+translated+'\n\n')
    
    #getting key
    with open('encrypted.txt') as f:
        cipher = f.read()
    key = findKey(cipher,myMessage)
    checkValidKey(key)
    print('One of the possible key is '+key.upper()+'\n\n')
    
    #decrypting message
    plain_txt = decryptMessage(key,cipher)
    print('Plain text obtained after decryption: '+plain_txt)
    

def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('This is not a valid monoalphabetic substitution cipher key!')

def encryptMessage(key, message):
    translated = ''
    charsA = LETTERS
    charsB = key
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated

def decryptMessage(key,message):
    plain = ''
    charsA = LETTERS
    charsB = key
    for symbol in message:
        if symbol.upper() in charsB:
            symIndex = charsB.find(symbol.upper())
            if symbol.isupper():
                plain += charsA[symIndex].upper()
            else:
                plain += charsA[symIndex].lower()
        else:
            plain += symbol
    return plain


def findKey(cipher,plain):
    chars = LETTERS
    key = [' ']*26
    for s in range(len(plain)):
        if plain[s].upper() in chars:
            idx = chars.find(plain[s].upper())
            key[idx]=cipher[s].upper()
            
    c2=[]
    for e in chars:
        if e in key:continue
        c2.append(e)
    
    for i in range(26):
        if key[i] == ' ':key[i]=c2.pop()
    
    return ''.join(key)
            
     

if __name__=="__main__":
    main()
