def indexing():
    le_string = "she sells sea shells on the sea shore"
    return len(le_string)

def concat():
    a = "cat "
    b = "tail"
    a = a + b 

    print(a)
    x = "age: " + str(18)
    print(x)

if __name__ == "__main__":
    concat()
    print(indexing())
