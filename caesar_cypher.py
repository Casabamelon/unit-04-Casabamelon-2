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
    
def encrypt_letter(letter, shift):
    #create a letter encrypter by converting letters to ASCII and differentiating the valies by [shift] amount
    letter = ord(letter)
    letter = int(letter) + shift
    letter = chr(int(letter))
    return letter 


def decrypt_message():
    plaintext = ""
    for letter in message:
        plaintext = plaintext + decrypt_letter



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
    # print(encrypt_letter("A", 3))
    # print(decrypt_letter("D", 3))
    # print(count_down(10))
    #input("enter a sentence (with spaces): ")
    print(encrypt_letter("A", 3))


# print(encrypt_letter("A", 3))
# print(decrypt_letter("D", 3))

# print("the \t brown fox \t jumped \n over the lazy dog")