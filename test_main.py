from main import counter

def test_true():
    assert True


ls = (
    {'Age': '23', 'Survived': '0', 'Sex': 'female', 'Pclass': '1'},
    {'Age': '23', 'Survived': '0', 'Sex': 'female', 'Pclass': '2'},
    {'Age': '23', 'Survived': '0', 'Sex': 'female', 'Pclass': '3'},

    {'Age': '23', 'Survived': '0', 'Sex': 'male', 'Pclass': '1'},
    {'Age': '23', 'Survived': '0', 'Sex': 'male', 'Pclass': '2'},
    {'Age': '23', 'Survived': '0', 'Sex': 'male', 'Pclass': '3'},

    {'Age': '23', 'Survived': '1', 'Sex': 'female', 'Pclass': '1'},
    {'Age': '23', 'Survived': '1', 'Sex': 'female', 'Pclass': '2'},
    {'Age': '23', 'Survived': '1', 'Sex': 'female', 'Pclass': '3'},

    {'Age': '23', 'Survived': '1', 'Sex': 'male', 'Pclass': '1'},
    {'Age': '23', 'Survived': '1', 'Sex': 'male', 'Pclass': '2'},
    {'Age': '23', 'Survived': '1', 'Sex': 'male', 'Pclass': '3'}
)

def test_counter():
    assert counter(ls) == (23, 23, 23, 23, 23, 23)

def test_counter_sex_female():
    assert counter(ls, sex='female') == (23, 23, 23, 23, 23, 23)

def test_counter_sex_male():
    assert counter(ls, sex='male') == (23, 23, 23, 23, 23, 23)

def test_counter_survived_0():
    assert counter(ls, survived='0') == (23, 23, 23, 23, 23, 23)

def test_counter_survived_1():
    assert counter(ls, survived='1') == (23, 23, 23, 23, 23, 23)
