def encrypt_letter(letter,shift):
    #I could use ascii values to shift integer values from one character to antoher
    if (is_alphabetic(letter)):
        letter = str(letter)
        asc = ord(letter)
    
        asc = int(asc) + int(shift)
        shift = chr(asc)
    return shift
    

def is_alphabetic(letter): 
    return letter >= "A" and letter <= "Z"


print(encrypt_letter("A", 3))