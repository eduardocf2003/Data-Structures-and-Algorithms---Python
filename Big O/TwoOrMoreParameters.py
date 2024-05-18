def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

    
#Nesse caso, por mais que pareça ser o mesmo caso de O(2n) que simplificamos para O(N), não podemos fazer
#isso pois temos dois parâmetros diferentes como entrada, nesse caso, a forma mais simplificada
#desse tipo de operação seria O(a+b)