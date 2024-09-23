def slice(string, stra, strb): #slice function
    charindex = int(stra) #creates ascending index
    substring = ""
    if strb > len(string):  
        strb = len(string) #sets second index to length of string if index value is too big
        while charindex < strb:
            substring = substring + string[charindex]
            charindex = charindex + 1 
        return substring
    elif strb < len(string):
        while charindex < strb:
            substring = substring + string[charindex]
            charindex = charindex + 1 
        return substring
    elif stra > strb: #returns nothing if first index is larger than second
        return "" 

 


def contains(string, substring):
    index = 0 


if __name__ == "__main__":
    print(slice("abcdef", 2, 4))
    print(contains("a dog", "dog"))