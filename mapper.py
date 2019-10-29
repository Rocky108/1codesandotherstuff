def lettertoindex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase+ ' '
    idx = alphabet.find(letter)
    if idx == -1:       #not found
        print("error:", letter, "is not the alphabet")
    return idx

def indextoletter(idx):
    from string import ascii_lowercase
    alphabet = ascii_lowercase+' '
    letter=''
    if idx>=len(alphabet):
        print("error:", idx, "is too large")
    elif idx<0:
        print("error:", idx, "is too small")
    else:
        letter= alphabet[idx]
    return letter