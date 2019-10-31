#transposition cipher

#original:This_is_a_secret_message_that_i_want_to_transmit
#encoded:hsi_ertmsaeta_att_rnmtti_sasce_esg_htiwn_otasi

def scramble2Encrypt(plaintext):
    evenChars= ""
    oddChars=""
    charCount= 0
    for ch in plaintext:
        if charCount % 2 == 0:
            evenChars=evenChars+ch
        else:
            oddChars=oddChars+ch
        charCount=charCount+1
    cipherText=oddChars+evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    halfLength=len(cipherText)//2
    evenChars=cipherText[halfLength:]
    oddChars=cipherText[:halfLength]
    plaintext=""

    for i in range(halfLength):
        plaintext= plaintext+evenChars[i]
        plaintext=plaintext+oddChars[i]

    if len(oddChars)<len(evenChars):
        plaintext=plaintext+evenChars[-1]

    return plaintext

# write a stripSpaces(text) function here

print(scramble2Encrypt("I am here"))

sentence="mhrIa ee"
print(sentence.replace(" ",""))



# write a cesarEncrypt(plainText, shift)
def encrypt(string,shift):
    cipher=''
    for char in string:
        if char==' ':
            chipher=cipher+char
        elif (char.isupper()):
            cipher+=chr((ord(char)+shift-65)%26+65)
        else:
            cipher+chr((ord(char)+shift-97)%26+97)
        return cipher
text="monmouth college fighting scots"
s=4

text = input("enter string: ")
s = int(input("enter shift number: "))
print("original string: ", text)
print("after encryption: ", encrypt(text, s))

# write a cesarDecrypt(cipherText, shift)
