import mystr

def test_slice(): #test 'normal'
    x = "cde"

    actual = mystr.slice("abcdef", 2, 4)

    assert actual == x

def test_slice(): #test for if index 2 is valued too high 
    x = "cdef"

    actual = mystr.slice("abcdef", 2, 10)

    assert actual == x

def test_slice(): #test for if index 1> index 2
    x = ""

    actual = mystr.slice("abcdef", 10, 4)

    assert actual == x