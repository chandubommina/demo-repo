def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("name: ")
    house = input("house: ")
    return name, house

if __name__ == '__main__':
    main()
