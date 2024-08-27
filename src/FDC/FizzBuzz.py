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

""""
for i in range(1,101):
    print(FizzBuzz(i),end="")
"""

print("Test valeur divisible par 3")
print("ATTENDU = Fizz | ENTREE = 3  | SORTIE = "+FizzBuzz(3))
print("ATTENDU = Fizz | ENTREE = 6  | SORTIE = "+FizzBuzz(6))
print("ATTENDU = Fizz | ENTREE = 21 | SORTIE = "+FizzBuzz(21))
print()

print("Test valeur divisible par 5")
print("ATTENDU = Buzz | ENTREE = 5  | SORTIE = "+FizzBuzz(5))
print("ATTENDU = Buzz | ENTREE = 10 | SORTIE = "+FizzBuzz(10))
print("ATTENDU = Buzz | ENTREE = 35 | SORTIE = "+FizzBuzz(35))
print()

print("Test valeur divisible par 3 et 5")
print("ATTENDU = FizzBuzz | ENTREE = 15 | SORTIE = "+FizzBuzz(15))
print("ATTENDU = FizzBuzz | ENTREE = 30 | SORTIE = "+FizzBuzz(30))
print("ATTENDU = FizzBuzz | ENTREE = 45 | SORTIE = "+FizzBuzz(45))
print()

print("Test valeur non divisible par 3 ou 5")
print("ATTENDU = (Valeur d'entrée) | ENTREE = 4  | SORTIE = "+FizzBuzz(4))
print("ATTENDU = (Valeur d'entrée) | ENTREE = 7  | SORTIE = "+FizzBuzz(7))
print("ATTENDU = (Valeur d'entrée) | ENTREE = 34 | SORTIE = "+FizzBuzz(34))
print()
