# 6.1
person_0 = {
    'first_name': 'esteban',
    'last_name': 'quito',
    'age': 38,
    'city': 'shotala',
}

person_1 = {
    'first_name': 'adrian',
    'last_name': 'diez canseco',
    'age': 26,
    'city': 'sucre',
}

person_2 = {
    'first_name': 'jhonny',
    'last_name': 'fernandez',
    'age': 54,
    'city': 'santa crux',
}

people = [person_0, person_1, person_2]

for person in people:

    for key, value in person.items():
        print(f"\n{key}: {value}")