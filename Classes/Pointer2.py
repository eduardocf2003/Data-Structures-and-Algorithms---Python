num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num1 =", num2)

print("\nnum1 points to:", id(num1))
print("\nnum2 points to:", id(num2))

num2 = 22
num1 = 13

print("After num2 value is updated:")
print("num1 =", num1)
print("num1 =", num2)

print("\nnum1 points to:", id(num1))
print("\nnum2 points to:", id(num2))

num1 = 11

print("\nnum1 points to:", id(num1))


#Nesse caso, podemos ver que o ponteiro irá apontar para outro endereço de memória, pois agora foi reservado
#um espaço para armazenar o valor de num2.

#Sempre que criamos um tipo de dado imutavel (integer ou string por exemplo), é tipicamente criado um endereço
#lifetime ou permanente para aquele valor na memória, sendo assim, mesmo havendo a substituição do valor em uma
#variável, o valor original continua existindo em um endereço na memória.

#No caso de linguagens como o Python e o Java, há um sistema de otimização chamado "interning" ou "pooling",
#esses mecanismos fazem com que possamos reaproveitar valores apontando para o mesmo endereço de memória original
#ou anterior.

#Por exemplo, se criarmos uma string com um valor, e depois criarmos outra com o mesmo valor, a linguagem pode
#optar por referenciar o mesmo endereço de memória do valor original, ao invés de criar um novo endereço.
