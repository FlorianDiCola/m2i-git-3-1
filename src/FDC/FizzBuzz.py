def FizzBuzz(entry):
    result = ""
    if entry % 3 == 0:
        result = "Fizz"
    if entry % 5 == 0:
        result = result+"Buzz"
    if result != "":
        return str(result)
    else:
        return str(entry)

for i in range(1,101):
    print(FizzBuzz(i),end="")