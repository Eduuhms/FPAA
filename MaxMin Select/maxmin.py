def maxmin_select(arr, inicio, fim):  # Definição da função de seleção simultânea de mínimo e máximo

    # Caso base: apenas um elemento
    if inicio == fim:  # Se o subarray tem apenas um elemento
        return arr[inicio], arr[inicio]  # Retorna esse elemento como mínimo e máximo

    # Caso base: dois elementos
    if fim == inicio + 1:  # Se o subarray tem dois elementos
        if arr[inicio] < arr[fim]:  # Compara os dois elementos
            return arr[inicio], arr[fim]  # Retorna na ordem (mínimo, máximo)
        else:
            return arr[fim], arr[inicio]  # Retorna na ordem (mínimo, máximo)

    # Divide o array ao meio
    meio = (inicio + fim) // 2  # Calcula o índice do meio
    min_esq, max_esq = maxmin_select(arr, inicio, meio)  # Chamada recursiva para metade esquerda
    min_dir, max_dir = maxmin_select(arr, meio + 1, fim)  # Chamada recursiva para metade direita

    # Combina os resultados das duas metades
    return min(min_esq, min_dir), max(max_esq, max_dir)  # Retorna o menor e maior entre as duas metades

