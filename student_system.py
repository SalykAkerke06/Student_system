# Студенттер тізімі жүйесі

students = []


def add_student():
    name = input("Аты-жөнін енгізіңіз: ")
    age = input("Жасын енгізіңіз: ")
    group = input("Тобын енгізіңіз: ")

    student = {
        "name": name,
        "age": age,
        "group": group
    }

    students.append(student)
    print("Студент сәтті қосылды!\n")


def show_students():
    if len(students) == 0:
        print("Тізім бос.\n")
    else:
        print("\nСтуденттер тізімі:")
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student['name']} | Жасы: {student['age']} | Тобы: {student['group']}")
        print()


def search_student():
    search_name = input("Ізделетін студенттің атын енгізіңіз: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nСтудент табылды:")
            print(f"Аты-жөні: {student['name']}")
            print(f"Жасы: {student['age']}")
            print(f"Тобы: {student['group']}\n")
            found = True

    if not found:
        print("Студент табылмады.\n")


def sort_students():
    students.sort(key=lambda x: x["name"])
    print("Студенттер аты бойынша сұрыпталды.\n")


def save_file():
    file = open("students.txt", "w", encoding="utf-8")

    for student in students:
        file.write(
            f"{student['name']} | {student['age']} | {student['group']}\n"
        )

    file.close()
    print("Мәліметтер students.txt файлына сақталды.\n")


while True:
    print("===== МӘЗІР =====")
    print("1 - Студент қосу")
    print("2 - Студенттер тізімін көрсету")
    print("3 - Студент іздеу")
    print("4 - Студенттерді сұрыптау")
    print("5 - Файлға сақтау")
    print("0 - Шығу")

    choice = input("Таңдауыңыз: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        sort_students()

    elif choice == "5":
        save_file()

    elif choice == "0":
        print("Бағдарлама аяқталды.")
        break

    else:
        print("Қате таңдау!\n")