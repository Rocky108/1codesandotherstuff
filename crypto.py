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
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = 3
plaintext = "Monmouth College"
ciphertext=""
for c in plaintext.upper():
    if c.isalpha(): ciphertext+=I2L[(L2I[c]+key)%26]
    else: ciphertext += c
print(plaintext)
print(ciphertext)
# write a cesarDecrypt(cipherText, shift)
decoded=""
for c in ciphertext.upper():
    if c.isalpha(): decoded += I2L[ (L2I[c]-key)%26]
    else: decoded += c

print(decoded)