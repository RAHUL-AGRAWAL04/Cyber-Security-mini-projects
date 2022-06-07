#Name              : Rahul Agrawal
#problem statement : 01(Transposition cipher)

#This function creates a matrix of r rows and c cols
def createMatrix(r,c):
	#length = len(plaintext)
	matrix = []
	for i in range(r):
		temp=[]
		for j in range(c):
			temp.append('$')
		matrix.append(temp)
	return matrix
    
# This function encrypts the plain message
def encrypt(plaintext,r,c):
	matrix= createMatrix(r,c)   
	cipher = ''
	counter = 0
	lenP = len(plaintext)
	for i in range(r):
		for j in range(c): 
			if counter == lenP or counter == r*c:
				break       
			matrix[i][j] = plaintext[counter]
			counter += 1
    
	for i in range(c):
		for j in range(r):
			cipher += matrix[j][i]
	
	if len(cipher) < len(plaintext):
		cipher += ''.join(plaintext[len(cipher):])
	return cipher
    
    
#This function decrypts the encrypted message
def decrypt(ciphertext,r,c):
	matrix = createMatrix(r,c)   
	plain = ''
	counter = 0
	lenC = len(ciphertext)
	cc = lenC//r
	if cc*r < lenC:
		cc += 1
	for i in range(cc):
		for j in range(r):
			if counter == lenC or counter == r*c:
				break
			matrix[j][i] = ciphertext[counter]
			counter += 1

	for i in range(r):
		for j in range(c):
			plain += matrix[i][j]
	plain += ''.join(ciphertext[len(plain):])
	temp = plain.split('$')
	plain = ''.join(temp)
	return plain
    


#DRIVER CODE
flag = -1
while flag!=0:
    print('Select Option\n[0] Exit\n[1] Encrypt\n[2] Decrypt')
    try:flag = int(input('>>>'))
    except:print('Select from the options provided.')
    if flag==0:
        break
    elif flag==1:
        plaintext = list(input('Plain Text : '))
        r, c = list(map(int,input('rows columns : ').split()))
        print('Encrypted message :',encrypt(plaintext,r,c)+'.')
    elif flag==2:
        ciphertext = list(input('Cipher Text : '))
        r, c = list(map(int,input('rows columns : ').split()))
        print('Decrypted message :',decrypt(ciphertext,r,c)+'.')
    else: print('Select from the options provided.')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
