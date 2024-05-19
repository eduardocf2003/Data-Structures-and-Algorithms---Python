num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num1 =", num2)

print("\nnum1 points to:", id(num1))
print("\nnum1 points to:", id(num2))

#Nesse caso, o ponteiro irá apontar para o mesmo lugar da memória e não criará outro espaço.