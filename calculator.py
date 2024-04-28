#calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return round(a/b,2)

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

flag = True
first = int(input("enter first number : "))
for i in operations:
    print(i)
while flag:
    op = input("pick an operation : ")
    second = int(input("enter next number : "))
    cal_function = operations[op]
    result = cal_function(first, second)
    print(f"{first} {op} {second} is {result}")
    again = input(f"type 'y' to continue with {result},or type 'n' to exit..").lower()
    if again == 'n':
        flag = False
        print("bye!")
    else:
        first = result

