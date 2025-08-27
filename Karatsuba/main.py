def karatsuba(x: int, y: int) -> int:
    # Caso base: se x ou y forem menores que 10, retorna a multiplicação direta
    if x < 10 or y < 10:
        return x * y

    # Determina o tamanho máximo dos números
    n = max(len(str(x)), len(str(y)))
    m = n // 2  # Divide o número no meio

    # Divide os números em duas partes
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)

    # Três chamadas recursivas
    r0 = karatsuba(low_x, low_y)
    r1 = karatsuba((low_x + high_x), (low_y + high_y))
    r2 = karatsuba(high_x, high_y)

    # Combina os resultados usando a fórmula de Karatsuba
    return (r2 * 10**(2*m)) + ((r1 - r2 - r0) * 10**m) + r0


if __name__ == "__main__":
    # Solicita os números ao usuário
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    resultado = karatsuba(a, b)
    print(f"\nResultado da multiplicação usando Karatsuba:")
    print(f"{a} * {b} = {resultado}")
