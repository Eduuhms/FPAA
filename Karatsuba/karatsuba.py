def karatsuba(x: int, y: int) -> int:  # Definição da função de multiplicação de Karatsuba

    if x < 10 or y < 10:  # Caso base: se x ou y forem menores que 10, retorna a multiplicação direta
        return x * y  # Multiplicação direta

    n = max(len(str(x)), len(str(y)))  # Converte os números em string para obter a quantidade de dígitos e armazenar a maior entre x e y
    m = n // 2  # Divide o número de dígitos no meio

    high_x, low_x = divmod(x, 10**m)  # Divide x em parte alta e baixa
    high_y, low_y = divmod(y, 10**m)  # Divide y em parte alta e baixa

    r0 = karatsuba(low_x, low_y)  # Primeira chamada recursiva, multiplicação da parte baixa
    r1 = karatsuba((low_x + high_x), (low_y + high_y))  # Segunda chamada recursiva, multiplicação das somas das partes
    r2 = karatsuba(high_x, high_y)  # Terceira chamada recursiva, multiplicação da parte alta

    return (r2 * 10**(2*m)) + ((r1 - r2 - r0) * 10**m) + r0  # Combina os resultados usando a fórmula de Karatsuba