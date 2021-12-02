def codigo():
    print (' escolha uma das opções abaixo')
    print ('1- dano estrutural (trinca) ')
    print ('2- dano superficial ')
    situacao = input (' opção: ')
    if situacao == '1':
        print (' Solução: ')
        print (' remover a área danificada ')
        print (' Confeccionar uma nova estrutura para a área que foi removida ')
        print (' Instalar a nova estrutura na fuselagem ')
        variavel = input('colocar medidas (mm): ')
        area = float (variavel)
        if area < 60.0:
            print (' retrabalhar area atraves de lixamento e aplicação de resina ')
        if 60 <= area and area <100.0:
            print (' usar 6 rebites ')
        if area >= 100.0 and area < 200.0:
            print (' usar 12 rebites ')
        if area >= 200.0 and area < 300.0:
            print (' usar 18 rebites ')
        if area >= 300.0 and area <= 400:
            print (' usar 24 rebites ')
        if area > 400:
            print (' substituir a superfície ')
        print()
        print (' voltando ao menu principal ')
        

    if situacao =='2':
        print (' Solução: ')
        print (' Remover o risco com lixa não muito abrasiva ')
        print (' Aplicação de pintura protetora anticorrosiva (primer) ')
        v = input ('colocar medidas (mm): ')
        a = float (v)
        if a < 60.0:
            print (' primer usado 20ml ')
        if a >= 60.0 and a < 100.0:
            print (' primer usado 30ml ')
        if a >= 100.0 and a < 200.0:
            print (' primer usado 50ml ')
        if a >= 200.0 and a < 300.0:
            print (' primer usado 70ml ')
        if a >= 300.0 and a <= 400.0:
            print (' primer usado 90ml ')
        if a > 400.0:
            print (' printura da superficie completa ')
        print (' Pintura final da fuselagem ')
        
        if a < 60.0:
            print (' tinta usada 20ml ')
        if a >= 60.0 and a <= 100.0:
            print (' tinta usada 30ml ')
        if a > 100.0 and a <= 200.0:
            print (' tinta  usada 50ml ')
        if a > 200.0 and a <= 300.0:
            print (' tinta  usada 70ml ')
        if a > 300.0 and a <= 400.0:
            print (' tinta  usada 90ml ')
        if a > 400.0:
            print (' printura da superficie completa ')
        print ()
        print (' voltando ao menu principal ')
        

