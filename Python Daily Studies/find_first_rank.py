students = [
    {'name': 'Priya', 'age': 99, 'rank': 5},
    {'name': 'Amma', 'age': 45, 'rank': 100},
    {'name': 'Arun', 'age': 29, 'rank': 2},
    {'name': 'Ranju', 'age': 50, 'rank': 4},
    {'name': 'Appa', 'age': 52, 'rank': 99}
]


def student_names():
    count = 0
    for i in students:
        print(i["name"])
        count += 1
    return "The number of students = " + str(count)

print(student_names())

def student_below30():
    name = ""
    for i in students:
        if i["age"] < 30:
            name += " " + i["name"]
            # print("student below 30 =", i["name"])
    print(name)

student_below30()
def student_above90():
    for i in students:
        if i["age"] > 90:
            print("student above 90 =", i["name"])


student_above90()

def low_rank():
    min_rank = students[0]
    for student in students:
        if min_rank["rank"] > student["rank"]:
            min_rank = student
    print(min_rank)


low_rank()


def high_rank():
    max = students[0]["rank"]
    for i in students:
        if max < i["rank"]:
            max = i["rank"]
    print(max)


high_rank()
# def main():
#     while True:
#         options = input(
#             "choose your option:\n a-student-names\nb-student_below30\nc-student_above90\nd-first_rank\ne-last_rank\ninput:")
#
#         if options == "a":
#             print(student_names())
#             elif
#         else:
#             break
#
#
# main()
