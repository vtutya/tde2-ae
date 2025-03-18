def iniciar():
    print('Area do triangulo: ')
    print('Area do retangulo: ')
    
    escolha = int(input('Escolha uma opção: '))
     
    if escolha == 1:
        triangulo()
    elif escolha == 2:
        retangulo()    
        
        
        
def triangulo():
    base = float(input('Digite a base do triangulo: '))
    altura = float(input('Digite a altura do triangulo: '))   
    area = (base * altura) / 2   
    print(area)
    iniciar() 
    
    
def retangulo():
    base = float(input('Digite a base do retangulo: '))
    altura = float(input('Digite a altura do retangulo: '))
    area = (base * altura)
    print(area)
    iniciar()

iniciar()