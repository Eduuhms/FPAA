from maxmin import maxmin_select  # Importa a função de seleção simultânea de mínimo e máximo

if __name__ == "__main__":  # Ponto de entrada do programa

    entrada = input("Digite os números da lista separados por espaço: ")  # Solicita ao usuário os números separados por espaço
    lista = [int(x) for x in entrada.split()]  # Converte a entrada em uma lista de inteiros

    print("Lista informada:", lista)  # Exibe a lista informada pelo usuário

    minimo, maximo = maxmin_select(lista, 0, len(lista) - 1)  # Chama a função para obter o menor e maior elemento

    print("Menor elemento:", minimo)  # Exibe o menor elemento
    print("Maior elemento:", maximo)  # Exibe o maior elemento
