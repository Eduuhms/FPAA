from karatsuba import karatsuba  # Importa a função do arquivo karatsuba.py

if __name__ == "__main__":  # Ponto de entrada do programa 

    a = int(input("Digite o primeiro número: "))  # Solicita o primeiro número ao usuário
    b = int(input("Digite o segundo número: "))  # Solicita o segundo número ao usuário

    resultado = karatsuba(a, b)  # Chama a função de Karatsuba para multiplicar os números
    print(f"\nResultado da multiplicação usando Karatsuba: {a} * {b} = {resultado}")  # Exibe o resultado da multiplicação
    
