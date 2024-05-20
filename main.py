import matplotlib.pyplot as plt
import streamlit as st
import csv

def counter(dc, survived='Любое', sex='Любой'):
    min_age = 200  # Гарантированно завышенное значение
    max_age = 0  # Гарантированно заниженное значение

    for row in dc:
        if row['Age'] == '':
            continue  # Если возраст не указан, считать нечего.

        if survived == 'Спасен (1)' and row['Survived'] == '0':
            continue  # Если поле "спасён" не совпадает не считаем.

        if survived == 'Погиб (0)' and row['Survived'] == '1':
            continue  # Если поле "спасён" не совпадает не считаем.

        if sex == 'Мужчина (male)' and row['Sex'] == 'female':
            continue  # Если поле "пол" не совпадает не считаем.

        if sex == 'Женщина (female)' and row['Sex'] == 'male':
            continue  # Если поле "пол" не совпадает не считаем.

        age = float(row['Age'])

        min_age = min(min_age, age)
        max_age = max(max_age, age)

    return min_age, max_age


st.header('Данные пассажиров Титаника')
st.image('Titanic_in_color.png')

st.write('Для просмотра данных только по спасенным или погибщим пассажирам, выберите соответствующий пункт из списка')
survived = st.selectbox('Значение поля Survived:', ['Любое', 'Спасен (1)', 'Погиб (0)'])

st.write('Для просмотра данных только по мужчинам или женщинам, выберите соответствующий пункт из списка')
sex = st.selectbox('Значение поля Sex:', ['Любой', 'Мужчина (male)', 'Женщина (female)'])

with open('data.csv') as file:
    reader = csv.DictReader(file)
    min_age, max_age = counter(reader, survived, sex)

data = {
    'Тип результата': ('минимум', 'максимум'),
    'Значение возраста': (min_age, max_age)
}
st.table(data)

type_return = ['минимум', 'максимум']
age = [min_age, max_age]

fig = plt.figure(figsize=(8, 3))
plt.bar(type_return, age)
plt.xlabel('Тип результата')
plt.ylabel('Возраст (поле Age)')
plt.title('Возраст пассажиров')

st.pyplot(fig)
