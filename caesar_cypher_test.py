import caesar_cypher

def test_encyrpt_letter():
    x = "D"
    expected = caesar_cypher.encrypt_letter("A",3)
    assert x == expected

def test_decrypt_letter():
    x = "A"
    expected = caesar_cypher.decrypt_letter("D",3)
    assert x == expected