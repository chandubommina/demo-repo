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

def calculator():
    flag = True
    first = float(input("enter first number : "))
    for i in operations:
        print(i)
    while flag:
        op = input("pick an operation : ")
        second = float(input("enter next number : "))
        cal_function = operations[op]
        result = cal_function(first, second)
        print(f"{first} {op} {second} is {result}")
        again = input(f"type 'y' to continue with {result},type 'n' to new start or type anything to exit : ").lower()
        if again == 'n':
            flag = False
            calculator()
        elif again == 'y':
            first = result
        else:
            break
calculator()
