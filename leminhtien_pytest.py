import pytest

def checkbcd(inb):
    if inb >= 0 and inb < 1001:
        return True
    else:
        return False

try:
    num = int(input("Input binary value: "), 2)
    checkbcd(num)
      
except ValueError:
    print("Please input only binary value.")

#Test
a_equal = 100
a_ans = True
b_1bigger = 1100
b_ans = False
c_empty = 123
c_ans = False
@pytest.mark.parametrize("x,y",[(a_equal,a_ans),(b_1bigger,b_ans),(c_empty,c_ans)])
def test_combine(x,y):
    assert y==checkbcd(x)
