# Projeto Karatsuba

O **Karatsuba** é um projeto desenvolvido para implementar e analisar o **Algoritmo de Karatsuba**, uma técnica eficiente de multiplicação de números inteiros grandes. Este algoritmo reduz o custo computacional da multiplicação em comparação ao método tradicional, sendo especialmente útil para operações com números muito extensos.  

---

## Sobre o Algoritmo de Karatsuba  

O **algoritmo de Karatsuba** foi introduzido em 1960 por Anatolii Karatsuba e revolucionou a forma como multiplicações grandes são tratadas.  
Enquanto o método tradicional possui complexidade **O(n²)**, o Karatsuba reduz essa complexidade para aproximadamente **O(n^log₂3) ≈ O(n^1.585)**, tornando-se muito mais eficiente para números grandes.  

A ideia central é dividir os números em duas partes e realizar apenas **três multiplicações recursivas**, em vez de quatro, como seria no método clássico.  

---

## Diferença entre Complexidade Assintótica e Complexidade Ciclomática  

- **Complexidade Assintótica:** mede o desempenho do algoritmo conforme o tamanho da entrada cresce.  
  - Melhor caso: O(1), quando os números são pequenos (ex.: < 10).  
  - Caso médio: O(n^1.585).  
  - Pior caso: também O(n^1.585).  

- **Complexidade Ciclomática:** mede a quantidade de caminhos independentes no código-fonte, importante para avaliar a necessidade de testes.  

---

## Como Executar o Projeto  

### 1. Clonar o repositório  
```bash
git clone https://github.com/Eduuhms/karatsuba.git
cd karatsuba
```

### 2. Executar o programa  
```bash
python main.py
```

O programa solicitará dois números ao usuário e exibirá o resultado da multiplicação utilizando o algoritmo de Karatsuba.  

---

## Versão do Python  

Este projeto foi desenvolvido e testado na versão **Python 3.13.5**.  

---

## Estrutura do Projeto  

**Arquivo: main.py**  
Objetivo: Implementa o algoritmo de Karatsuba e realiza a multiplicação de dois números inteiros inseridos pelo usuário.  

### Funções:  

#### `karatsuba(x, y)`  
- **Parâmetros:** dois inteiros `x` e `y`.  
- **Retorno:** resultado da multiplicação usando o algoritmo de Karatsuba.  
- **Lógica:**  
  1. Verifica caso base (se `x` ou `y < 10`, multiplica diretamente).  
  2. Divide os números em duas partes (alta e baixa).  
  3. Calcula três multiplicações recursivas: `r0`, `r1` e `r2`.  
  4. Combina os resultados usando a fórmula de Karatsuba.  

#### `main`  
- Solicita dois números ao usuário.  
- Chama a função `karatsuba(x, y)`.  
- Exibe o resultado formatado.  

---

## Relatório Técnico  

### Complexidade Assintótica  
- **Tempo:** O(n^log₂3) ≈ O(n^1.585).  
- **Espaço:** O(n), devido ao uso da recursão e armazenamento temporário das variáveis intermediárias.  

### Complexidade Ciclomática  
A função `karatsuba` possui **3 estruturas condicionais/decisões principais**, resultando em uma complexidade ciclomática relativamente baixa, mas suficiente para exigir múltiplos testes (casos pequenos, médios e grandes).  

---

## Exemplo de Execução  

```bash
Digite o primeiro número: 123456789
Digite o segundo número: 987654321

Resultado da multiplicação usando Karatsuba:
123456789 * 987654321 = 121932631112635269
```

---

## Grafo de Fluxo da Função `karatsuba`

![Fluxo Karatsuba](fluxo_karatsuba.png)
