#Name              : Rahul Agrawal
#problem statement : 02(One Time Pad)

#######################################################

alphabet = "abcdefghijklmnopqrstuvwxyz 1234567890`-=~!@#$%^&*()_+{}:\"<>?,./;'[]\|"
size = len(alphabet)

#encodes single character. Used bt encrypt function.
def encodeChar(plainChar, key):	
    charNum = ( alphabet.find(plainChar) + alphabet.find(key) ) % size
    cipherChar = alphabet[charNum]
    return cipherChar

#decodes single character. Used bt decrypt function.
def decodeChar(cipherChar, key): 
    plainNum = alphabet.find(cipherChar) - alphabet.find(key)
    plainChar= alphabet[plainNum]
    return plainChar

#encrypts the plain message
def encrypt(plainText, key):	
    key = processKey(key,len(plainText)) #key balancing
    cipherText= ''
    for i in range(0, len(plainText)):
        cipherText += encodeChar(plainText[i], key[i])

    return cipherText

#decrypts the encrypted message.
def decrypt(cipherText, key): 
    key = processKey(key,len(cipherText))	#key balancing
    plainText=''
    for i in range(0, len(cipherText)):
        plainText += decodeChar(cipherText[i], key[i])
    return plainText

#This function ensure that key length >= message length.
def processKey(key,length):	
    while len(key)<length:
        if len(key)-length < length:
            key += key[:length - len(key)]
        else:
            key += key
    return key


#DRIVER CODE
print('OTP Program. Key may be of any length.')
print('Plaintext may contain Alphabet, Numbers, Special character.')

flag = -1
while flag!=0:
    print('Select Option\n[0] Exit\n[1] Encrypt\n[2] Decrypt')
    try:flag = int(input('>>>'))
    except:print('Select from the options provided.')
    if flag==0:
        break
    elif flag==1:
        plaintext = input('Plain Text : ')
        key = input('Key : ')
        print('Encrypted message :',encrypt(plaintext.lower(),key)+'.')
    elif flag==2:
        ciphertext = input('Cipher Text : ')
        key = input('Key : ')
        print('Decrypted message :',decrypt(ciphertext.lower(),key)+'.')
    else: print('Select from the options provided.')













