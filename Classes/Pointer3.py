dict1 = {
    'value': 11
}

dict2 = dict1

print("Before value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("\ndict2 points to:", id(dict2))

dict2['value'] = 22

print("After value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("\ndict2 points to:", id(dict2))

#Nesse caso, temos um objeto mutavel, um dicionário.

#Por ser mutável, ao modificarmos um dicionário, ele seguirá apontando para o mesmo endereço de memória.
#Isso quer dizer que por ser mutável, ele é capaz de modificar sem precisar criar e apontar para um novo endereço,
#Ou seja, mesmo que haja um mecanismo de otimização, não existe uma referencia do dicionário original na memória

#Suponhamos que existem 3 dicionários (ou objetos mutaveis) com valores diferentes, chamados d1, d2 e d3.
#Se decidirmos apontar d1 para d2 e d2 para d3, no final teremos todos apontando para o mesmo endereço(d3).
#Isso irá fazer com que os valores originais de d1 e d2 deixem de existir na memória, pois serão eliminados
#pelo garbage collector.

#A fim de ilustrar, podemos descrever um dicionario como um grupo de amigos no whatsapp,
#nele você pode adicionar e remover as pessoas, porém, no final continua sendo o mesmo grupo (mesmo endereço),
#porém, você não tem mais uma referência de como era aquele grupo originalmente.

#Vale lembrar que caso popularmos um dicionario com valores imutáveis, apenas o dicionário que apontava para eles
#deixa de existir, os valores imutaveis seguem dispostos na memória podendo serem referenciados novamente.

#Para ilustrar os objetos imutaveis, pode-se utilizar o exemplo de uma parede que foi pintada de outra cor.
#Suponhamos que uma parede (variável) azul (objeto imutável) foi coberta por uma tinta de cor verde.
#Mesmo que a parede agora esteja verde, a tinta azul continua existindo, porém, não é mais a cor daquela parede.
#Se trouxessemos para nosso contexto, a parede agora aponta para o endreço que foi criado para a cor verde, porém
#a cor azul continua existindo no mesmo endereço, porém, sem ser apontada.