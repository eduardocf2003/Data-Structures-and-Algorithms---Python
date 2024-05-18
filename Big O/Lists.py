#Supondo que há uma lista com numeros ordenados ou não de 4 elementos (variando da posição 0 a 3).

#Caso precisarmos inserir (append) ou remover (pop) um elemento ao fim dessa lista, teremos a complexidade O(1).

#Caso precisarmos inserir ou remover um elemento na primeira posição da lista (0), a complexidade será de
#O(n), pois teremos que movimentar todos os outros elementos para uma posição a mais (no caso de um append)
#ou a menos (no caso de um pop).

    #Caso seja necessário inserir um numero em qualquer outra posição da lista, poderiamos pensar que a complexidade
#correta seria O(1/2 n), porém, isso está errado por dois motivos.
#O primeiro motivo, é que em Big O, sempre consideramos o PIOR caso, ou seja, o que teria maior custo computacional
#Ou seja, 1/2 n significaria que no pior caso, o numero de operações seria igual a metade do numero de elementos da
#lista, porém, se tivermos uma lista de 10 elementos e precisarmos incluir um elemento na posição 1, seria
#necessário mover todos os elementos da posição 1 a 9, ou seja. 9 operações.
    #O segundo motivo é simples, como em big o sempre calculamos o crescimento do custo de poder computacional
#com base no tamanho ou quantidade de entradas, a constante 1/2 se torna irrelevante.
    #Sendo assim, a operação correta se mostra O(n).


#Caso precisarmos procurar um item na lista utilizando seu valor como parâmetro, 
#a complexidade em big o é dada pela notação O(n

#Caso precisarmos procurar um item na lista pelo seu index, a complexidade é de O(1), pois conseguimos acessá-lo
#diretamente na memória.