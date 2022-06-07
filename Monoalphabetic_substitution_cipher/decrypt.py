import sys
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#myKey =  'QWERTYUIOPASDFGHJKLZXCVBNM'

def main():
    #myMessage = 'To be, or not to be, that is the question.'
    myMessage = 'Zg wt, gk fgz zg wt, ziqz ol zit jxtlzogf.'
    myKey = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    checkValidKey(myKey)
    plain_txt = decryptMessage(myKey,myMessage)
    print(plain_txt)

def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('This is not a valid monoalphabetic substitution cipher key!')

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

if __name__=="__main__":
    main()
