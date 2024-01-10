def main():
    student = get_student()
    if student["name"] == 'druva':
        student["house"] = "bommini"
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("name: ")
    student["house"] = input("house: ")
    return student

if __name__ == '__main__':
    main()
