students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(name):
    try:
        return students[name]
    except KeyError:
        return 'Student not found'

test_students = ['John', 'Jane', 'Doe', 'Jerry']

for student in test_students:
    print(get_age(student))

