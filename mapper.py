def lettertoindex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase+ ' '
    idx = alphabet.find(letter)
    if idx == -1:       #not found
        print("error:", letter, "is not the alphabet")
    return idx

