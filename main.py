import matplotlib.pyplot as plt
import streamlit as st
import csv

def counter(ls, survived='Любое', sex='Любой'):
    min_1cl, min_2cl, min_3cl = 200, 200, 200  # Гарантированно завышенные значения
    max_1cl, max_2cl, max_3cl = 0, 0, 0  # Гарантированно заниженные значения

    for row in ls:
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

        if row['Pclass'] == '1':
            min_1cl = min(min_1cl, age)
            max_1cl = max(max_1cl, age)

        elif row['Pclass'] == '2':
            min_2cl = min(min_2cl, age)
            max_2cl = max(max_2cl, age)

        elif row['Pclass'] == '3':
            min_3cl = min(min_3cl, age)
            max_3cl = max(max_3cl, age)

        else:
            st.write('Обнаружен неопознанный класс обслуживания клиентов.')

    return min_1cl, min_2cl, min_3cl, max_1cl, max_2cl, max_3cl


st.header('Данные пассажиров Титаника')
st.image('Titanic_in_color.png')

st.write('Для просмотра данных только по спасенным или погибщим пассажирам, выберите соответствующий пункт из списка')
survived = st.selectbox('Значение поля Survived:', ['Любое', 'Спасен (1)', 'Погиб (0)'])

st.write('Для просмотра данных только по мужчинам или женщинам, выберите соответствующий пункт из списка')
sex = st.selectbox('Значение поля Sex:', ['Любой', 'Мужчина (male)', 'Женщина (female)'])

with open('data.csv') as file:
    reader = csv.DictReader(file)
    min_1cl, min_2cl, min_3cl, max_1cl, max_2cl, max_3cl = counter(reader, survived, sex)

####################

pclass = ['1 класс', '2 класс', '3 класс']
age_min = [min_1cl, min_2cl, min_3cl]
age_max = [max_1cl, max_2cl, max_3cl]
data = {
    'Класс обслуживания': pclass,
    'Минимальный возраст': age_min,
    'Максимальный возраст': age_max
}
st.table(data)

fig = plt.figure(figsize=(8, 3))
plt.bar(pclass, age_max, bottom=age_min)
plt.xlabel('Значение поля Pclass')
plt.ylabel('Возраст (поле Age)')
plt.title('Возраст пассажиров по классам обслуживания')

st.pyplot(fig)
