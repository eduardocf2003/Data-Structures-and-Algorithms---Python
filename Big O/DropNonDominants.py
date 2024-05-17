def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)


print_items(10)

#Nesse caso, teriamos uma notação O(n²+n), porém, podemos omitir o segundo n, pois ao lidarmos com entradas
#de valores maiores, seu valor seria insignificante para a equação dado o crescimento exponencial de n².
#Podemos ver um exemplo claro no codigo acima, onde o n² representa um total de 100 operações e n apenas 10.
#É ainda mais insignificante quando observamos valores como n = 100, onde n² representaria 10.000 enquanto
#n apenas 100.