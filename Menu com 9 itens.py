import sys
lista=[]
print('*****************************************************')
print('\n')
print("ESCOLHA UMA OPÇÃO:")
print('\n')
print("   1-Cadastra um Amigo                               ")
print("   2-Mostrar os Nomes de todos os Amigos             ")
print("   3-Cadastrar um amigo (início da lista)            ")
print("   4-Remover um nome                                 ")
print("   5-Substituir um nome                              ")
print("   6-Mostrar o número total de amigos cadastrados    ")
print("   7- Colocar os nomes dos amigos em ordem alfabética")                                      
print("   9-Sair                                            ")
print('\n')
print('*****************************************************')


while True:
 op=input("Digite a Opção:")
 
 if op == '1':
    
   nome=input("Insira o Nome:")
   lista.append(nome)
   print("Nome Confirmado", nome)
 
    
 if op == '2':
     
   for p in lista:
    print("Menbros da Lista:", end='-')
    print(p)
    
    
 if op == '3':
    nome=input("Insira o Nome no inicio da fila:")
    lista.insert(0,nome)
    
    
 if op == '4':
    print('O indice do nome a ser excluido:')
    for i in enumerate(lista):
     print(i)
    i=int(input('Informe o indice a ser excluido'))
    del lista [i]
    print("Nova Lista com a Remoção",lista)
    
    
 if op == '5':
    print('O indice do nome a ser Substituido:')
    for i in enumerate(lista):
     print(i)
    i=int(input('Informe o indice a ser Substituido'))
    nome=input("Insira o Novo Nome:")
    lista[i] = nome
    print ('Nova lista com a Substituição do Nome', lista)
    
    
 if op== '6':
    print('O total de membros da Lista:', len (lista))
    
    
 if op == '7':
    print ('Ordem Alfabética dos membros da lista:')
    lista.sort ()
    print (lista)
    
    
     
 if op == '9':
    
    exit()
            
