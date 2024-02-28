import simple

def test_addition():
    assert simple.addition(3, 5) == 8
    assert simple.addition(0, 0) == 0
    assert simple.addition(-1, 1) == 0

def test_multiplication():
    assert simple.multiplication(3, 5) == 15
    assert simple.multiplication(0, 5) == 0
    assert simple.multiplication(-1, -1) == 1

def test_division():
    assert simple.division(10, 2) == 5
    assert simple.division(5, 2) == 2.5

def test_modulus():
    assert simple.modulus(10, 3) == 1
    assert simple.modulus(7, 2) == 1
