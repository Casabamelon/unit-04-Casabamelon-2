def encrypt_letter(letter,shift):
    #I could use ascii values to shift integer values from one character to antoher
    if (is_alphabetic(letter)):
        letter = str(letter)
        asc = ord(letter)
    
        asc = int(asc) + int(shift)
        shift = chr(asc)
        return shift
    
#def enrypt_message(message,shift):

def count_down(count):
    sum = 0
    while count > 0:
        print(count)
        sum = sum + count
        count = count - 1
    return sum
    
def decrypt_letter(letter,shift):
    #create a sinilar function to encrypt except ascii values are subtracted 
    if (is_alphabetic(letter)):
        letter = str(letter)
        asc = ord(letter)
    
        asc = int(asc) - 3
        shift = chr(asc)
    return shift

def is_alphabetic(letter): 
    return letter >= "A" and letter <= "Z"

if __name__ == "__main__":
    print(encrypt_letter("A", 3))
    print(decrypt_letter("D", 3))
    print(count_down(10))


# print(encrypt_letter("A", 3))
# print(decrypt_letter("D", 3))

# print("the \t brown fox \t jumped \n over the lazy dog")