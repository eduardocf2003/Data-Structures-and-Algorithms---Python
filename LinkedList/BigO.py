#Big O de uma Linked List

#A complexidade de inserir um elemento no fim da lista é O(1), pois independente da quantidade de elementos
#na lista, sempre precisarermos apenas apontar o ultimo numero da lista ao novo numero e transferir a cauda.

#Para remover um elemento do fim da lista, a complexidade é O(N), isso acontece pois os elementos em uma linked list
#se ligam apenas ao próximo elemento, ou seja, um elemento "não sabe" qual elemento antecede ele, apenas o sucessor.
#Sendo assim, precisamos percorrer toda a lista novamente para encontrar o ultimo elemento,
#onde iremos apontar a cauda.

#Para adicionar elementos ao inicio da lista, temos a complexidade O(1), pois seguimos os mesmos principios
#da adição no fim da lista.

#Para remover elementos do inicio da lista, ao contrário de quando removemos do fim, o elemento a ser removido
#"Sabe" qual é o próximo elemento da lista (pois está apontando para ele), com isso, o ponteiro "Head"
#sabe exatamente para onde apontar no caso da retirada do elemento inicial. Complexidade O(1).

#Ao adicionar um item no meio da lista, temos a complexidade O(n), pois como não há indices, precisamos percorrer
#toda a estrutura até encontrar o nó do numero, que agora apontará para um novo numero.

#Ao remover um item no meio da lista, precisamos percorrer a lista até encontrar o valor a ser removido e então,
#replicar o ponteiro do item removido no item anterior. Complexidade O(n)

#Para buscar um item em uma Linked List, podemos percorrer a lista até encontrar o valor desejado ou
#percorrer a lista até chegar no índice desejado, não sendo possível acessar diretamente. Complexidade O(n)

