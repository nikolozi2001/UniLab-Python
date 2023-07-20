# import random

# yes = random.randint(30,200)
# no = random.randint(30,200)
# pop = yes + no
# yes_share = yes * 100/pop
# no_share = no * 100/pop
# YES = f'YES: {yes} = {yes_share:.2f}%'
# NO = f'NO: {no} = {no_share:.2f}%'
# print(YES)
# print(NO)

# number = 1

# while number <= 10:
#     print(f"{number} is")
#     if number % 2 == 0:
#         print("ლუწი")
#     else:
#         print("კენტი")
#     number += 1


import random

students = {
    "სალომე": [random.randint(40, 100) for _ in range(5)],
    "თორნიკე": [random.randint(40, 100) for _ in range(5)],
    "ანასტასია": [random.randint(40, 100) for _ in range(5)],
    "გიორგი": [random.randint(40, 100) for _ in range(5)],
    "სანდრო": [random.randint(40, 100) for _ in range(5)],
}

# ხელმისაწვდომი საშუალო არითმეტიკული ქულა
def calculate_average(grades):
    return sum(grades) / len(grades)

# შესაფერისი ნიშანის დაბრუნება
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"

# ყველა სტუდენტის შესაბამისი ქულების დაბრუნება
def get_student_grades(students):
    student_grades = {}
    for student, grades in students.items():
        student_grades[student] = grades
    return student_grades

# ყველა სტუდენტის არითმეტიკული ქულას გამოთვლა
def calculate_student_averages(student_grades):
    student_averages = {}
    for student, grades in student_grades.items():
        average_grade = calculate_average(grades)
        student_averages[student] = average_grade
    return student_averages

# ყველა სტუდენტის ნიშნის დაბრუნება
def calculate_student_letter_grades(student_averages):
    student_letter_grades = {}
    for student, average in student_averages.items():
        letter_grade = get_letter_grade(average)
        student_letter_grades[student] = letter_grade
    return student_letter_grades

# ყველა სტუდენტის ქულების დაბრუნება
def print_student_grades(student_grades):
    for student, grades in student_grades.items():
        print(f"{student} - ქულები: {grades}")

# ყველა სტუდენტის შესაბამისი არითმეტიკული ქულა და ნიშანის დაბრუნება
def print_student_averages_and_grades(student_averages, student_letter_grades):
    for student, average in student_averages.items():
        letter_grade = student_letter_grades[student]
        print(f"{student} - არითმეტიკული ქულა: {average:.2f}, ნიშანი: {letter_grade}")

# სტუდენტების ქულების და ნიშანების დაბეჭდვა
def print_students_grades_and_averages(students):
    student_grades = get_student_grades(students)
    print("ყველა სტუდენტის ქულები:")
    print_student_grades(student_grades)

    student_averages = calculate_student_averages(student_grades)
    student_letter_grades = calculate_student_letter_grades(student_averages)

    print("\nყველა სტუდენტის არითმეტიკული ქულა:")
    print_student_averages_and_grades(student_averages, student_letter_grades)

print_students_grades_and_averages(students)
