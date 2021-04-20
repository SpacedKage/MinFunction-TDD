from min_func import min

def test_min_normal_values():
   assert min(3, 6) == 3

def test_min_negative_value():
    assert min(2, -1) == -1

def test_min_same_value():
    assert min (9, 9) == 9
