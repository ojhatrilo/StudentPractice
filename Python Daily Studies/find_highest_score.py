students = [
    {
        'name': 'Priya',
        'age': 99,
        'rank': 5,
        "marks": {
            "physics": 30,
            "maths": 50,
            "chemistry": 70,
        }
    },
    {
        'name': 'Amma',
        'age': 45,
        'rank': 100,
        "marks": {
            "physics": 22,
            "maths": 60,
            "chemistry": 12,
        }
    },
    {
        'name': 'Arun',
        'age': 29,
        'rank': 2,
        "marks": {
            "physics": 99,
            "maths": 98,
            "chemistry": 100,
        }
    },
    {
        'name': 'Ranju',
        'age': 50,
        'rank': 4,
        "marks": {
            "physics": 12,
            "maths": 15,
            "chemistry": 35,
        }
    },
    {
        'name': 'Appa',
        'age': 52, 'rank': 99,
        "marks": {
            "physics": 45,
            "maths": 34,
            "chemistry": 90
        }
    }
]


def find_highest_scored():
    
    for student in students:
        highest_mark = None
        highest_subject = None
        student_name = None
        for subject, mark in student["marks"].items():
            if (highest_mark is None) or highest_mark < mark:
                highest_mark = mark
                highest_subject = subject
                student_name = student["name"]
        print(f"{student_name} has scored the highest mark of {highest_mark} in {highest_subject}")
        # print(highest_mark)
        # print(highest_subject)
        # print(student_name)


find_highest_scored()


def find_lowest_scored():
    for student in students:
        lowest_mark = None
        lowest_subject = None
        student_name = None
        for subject, mark in student["marks"].items():
            if (lowest_mark is None) or lowest_mark > mark:
                lowest_mark = mark
                lowest_subject = subject
                student_name = student["name"]
        print(f"{student_name} has scored the highest mark of {lowest_mark} in {lowest_subject}")
        # print(highest_mark)
        # print(highest_subject)
        # print(student_name)


find_lowest_scored()



