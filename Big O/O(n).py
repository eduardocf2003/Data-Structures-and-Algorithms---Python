def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

#A notação O(n) ocorre sempre em que o numero de operações for igual a n.
#Caso tenhamos um algoritmo atrelado a uma constante, ex O(2n), podemos omitir a constante, pois nosso
#o objetivo é analisar a complexidade de acordo com o tamanho da entrada. Como temos uma constante, o crescimento 
#continuará sendo linear, o que não afeta tanto em nossa análise.
#Outro ponto para omitirmos a constante, é que quando lidamos principalmente com valores grandes, o impacto 
#causado na performance é irrelevante, principalmente quando comparada com por exemplo o(n²), que pode trazer
#sérios problemas de performance quando n está na casa de milhão ou bilhão.