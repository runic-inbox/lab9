from main import counter

def test_true():
    assert True


ls = (
    {'Age': '11', 'Survived': '0', 'Sex': 'female'},
    {'Age': '22', 'Survived': '0', 'Sex': 'female'},
    {'Age': '', 'Survived': '0', 'Sex': 'female'},

    {'Age': '33', 'Survived': '0', 'Sex': 'male'},
    {'Age': '44', 'Survived': '0', 'Sex': 'male'},
    {'Age': '', 'Survived': '0', 'Sex': 'male'},

    {'Age': '55', 'Survived': '1', 'Sex': 'female'},
    {'Age': '66', 'Survived': '1', 'Sex': 'female'},
    {'Age': '', 'Survived': '1', 'Sex': 'female'},

    {'Age': '77', 'Survived': '1', 'Sex': 'male'},
    {'Age': '88', 'Survived': '1', 'Sex': 'male'},
    {'Age': '', 'Survived': '1', 'Sex': 'male'}
)

def test_counter():
    assert counter(ls) == (11, 88)

def test_counter_sex_female():
    assert counter(ls, sex='Женщина (female)') == (11, 66)

def test_counter_sex_male():
    assert counter(ls, sex='Мужчина (male)') == (33, 88)

def test_counter_survived_0():
    assert counter(ls, survived='Погиб (0)') == (11, 44)

def test_counter_survived_1():
    assert counter(ls, survived='Спасен (1)') == (55, 88)
