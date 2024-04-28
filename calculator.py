#calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

first = int(input("enter first number : "))
second = int(input("enter second number : "))
for i in operations:
    print(i)
op = input("choose operation : ")
cal_function = operations[op]
result = cal_function(first, second)
print(f"{first} {op} {second} is {result}")

