
def get_student_report(students):
    print("Generating Report For Each Individual Student...")
    english_class = []
    math_class = []
    science_class = []
    failed_students = 0

    for student , result in students.items():
        print(f"\nStudent Name : {student}\nStudent Result Card:")

        for subject_name , marks in result.items():
            if marks >= 35:
                print(f"{subject_name} : {marks}")

            elif marks < 35:
                print(f"{subject_name} : {marks}. {student} has failed {subject_name}")
                failed_students += 1
                if subject_name == 'English':
                    english_class.append(student)
                    english_class.append(subject_name)
                    english_class.append(marks)

                elif subject_name == 'Maths':
                    math_class.append(student)
                    math_class.append(subject_name)
                    math_class.append(marks)

                elif subject_name == 'Science':
                    science_class.append(student)
                    science_class.append(subject_name)
                    science_class.append(marks)

    total_failed_students = len(english_class + math_class + science_class)
    print('\nStudents who have failed:\n')

    if len(english_class) > 0:
        for i in english_class:
            print(i)
        print("Student has been sucessfully added to the improvement class!\n")

    if len(math_class) > 0:
        for i in math_class:
            print(i)
        print("Student has been added to the improvement class!\n")


    if len(science_class) > 0:
        for i in science_class:
            print(i)
        print("Student has been added to the improvement class!\n")


students = {

    "Rozail" :{"English" : 77, "Maths" : 18, "Science" : 44},
    "Alice" : {"English" : 33, "Maths" : 94, "Science" : 88},
    "James" : {"English" : 88, "Maths" : 39, "Science" : 88},
    "Sonic" : {"English" : 88, "Maths" : 98, "Science" : 81}

}

get_student_report(students)