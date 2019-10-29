#transposition cipher

#original:This_is_a_secret_message_that_i_want_to_transmit
#encoded:hsi_ertmsaeta_att_rnmtti_sasce_esg_htiwn_otasi

defscramble2encrypt(plaintext)
evenChars= ""
oddChars=""
charCount= 0
    for ch in plaintext:
        if charCount %2==0
            evenChars=evenChars+ch
        else:
            oddChars=oddChars+ch
        charCount=charCount+1
    cipherText=oddChars+evenChars
    return cipherText