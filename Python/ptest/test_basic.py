from basicmath import div

# pip install pytest
# py.test to run all python scripts starting with test_

def test_div():
    assert div(4, 2) == 2 

def test_div2():
    assert div(15, 3) == 5

# fails if python 2 but passes python 3 (integer division)
def test_div_for_float():
    assert div(1, 2) == 0.5 

 


