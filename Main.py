import Model
situacao = ' '
while situacao != '3':
    #menu do sistema
    print('1) executar programa')
    print ('2) ajuda ')
    print ('3) sair')

    situacao = str(input('situacao: '))
    if situacao == '3':
        print('saindo do sistema')
        

    #caso a opção escolhida seja 1, executar o programa
    elif situacao == '1':
        Model.codigo()

       

    elif situacao == '2':
        print (' funções do programa ')
        print (' 1 executar: essa é uma função, que ao digitar 1, você terá acesso aos procedimentos que devem ser utilizados para o reparo dos danos mostrados (no caso: dano estrutural e superficial) ')
        print (' Dentro da função executar são mostradas duas opções, escolha uma delas para ter informações deste processo de reparação ')
        print (' ajuda: onde são explicadas as outras funções deste programa ')
        print (' 3- sair: sairá do programa, deixando-o assim, pronto para ser fechado, e finalizando as outras funções ')
        print (' colocar a medida da area: mantendo a unidade em milimetro ') 
        print ()
        print (' voltando ao menu principal ')

    else:
        print (' opção inválida ')
        
        
            
