import os

def iniciar():
    print('1. Área do triangulo: ')
    print('2. Área do retangulo: ')
    print('3. Área do quadrado: ')
    print('4. Área do círculo: ')
    print('5. Sair')
    
    escolha = int(input('Escolha uma opção: '))

    while True:
        if escolha == 1:
            triangulo()
        elif escolha == 2:
            retangulo()
        elif escolha == 3:
            quadrado()      
        elif escolha == 4:
            circulo() 
        elif escolha == 5:
            saindo() 
            break
        else:
            print('Opção inválida, tente novamente')    
            iniciar()
                
        
        
        
def triangulo():
    base = float(input('Digite a base do triangulo: '))
    altura = float(input('Digite a altura do triangulo: '))   
    area = (base * altura) / 2   
    print(f'A área do triângulo é: {area}')
    iniciar() 
    
    
def retangulo():
    base = float(input('Digite a base do retangulo: '))
    altura = float(input('Digite a altura do retangulo: '))
    area = (base * altura)
    print(f'A área do retângulo é: {area}')
    iniciar()

def quadrado():
    lado = float(input('Digite o lado do quadrado: '))
    lado = lado**2
    print(f'A área do quadrado é: {lado}')
    iniciar()

def circulo():
    pi = 3.14159
    raio = float(input('Digite o raio do círculo: '))
    area = (raio**2) * pi
    print(f'A área do círculo é: {area}')
    iniciar()

def saindo():
    os.system('cls')
    print('Saindo...')
    


iniciar()