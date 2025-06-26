# CS50
Repositório para guardar os códigos desenvolvidos no curso de Ciência da Computação CC50.


## Modulo 1: Linguagem C Exercicios:

### 1. Mario
O programa que escreveremos se chamará mario. E vamos permitir que o usuário decida qual deve ser a altura da pirâmide, primeiro solicitando um número inteiro positivo entre, digamos, 1 e 8.

Exemplo:
   #
   ##
   ###
   ####

### 2. Mario Desafio

O programa que escreveremos se chamará mario. E vamos permitir que o usuário decida a altura das pirâmides, primeiro solicitando um número inteiro positivo entre, digamos, 1 e 8.

Exemplo:
   #  #
  ##  ##
 ###  ###
####  ####

### 3. Dinheiro

mplemente, em um arquivo chamado cash.c em um diretório ~/pset1/cash, um programa que pergunta ao usuário quanto dinheiro é devido e em seguida imprime o número mínimo de moedas com as quais essa troca pode ser feita.

Use get_float para obter a entrada do usuário e printf para gerar sua resposta. Suponha que as únicas moedas disponíveis sejam de 25, 10, 5 e 1 centavo(s).

### 4. Credito Desafio

Então, qual é a fórmula secreta? Bem, a maioria dos cartões usa um algoritmo inventado por Hans Peter Luhn, da IBM. De acordo com o algoritmo de Luhn, você pode determinar se um número de cartão de crédito é (sintaticamente) válido da seguinte maneira:

- Multiplique cada segundo digito por 2, começando com o penúltimo dígito do número e, em seguida, some os dígitos desses produtos.
- Adicione essa soma à soma dos dígitos que não foram multiplicados por 2.
- Se o último dígito do total for 0 (ou, mais formalmente, se o módulo total 10 for congruente com 0), o número é válido!

### 5. Populaçao Desafio

Você deve implementar um programa que:

1. Solicite ao usuário:
- Um tamanho inicial da população (≥9 lhamas)
- Um tamanho final da população (≥ tamanho inicial)

2. Valide as entradas:
- Se o valor inicial for <9, repita a solicitação
- Se o valor final for menor que o inicial, repita a solicitação

3. Calcule quantos anos são necessários para:
A população crescer do tamanho inicial ao final

Considerando que a cada ano:
- Nascem n/3 lhamas (arredondado para baixo)
- Morrem n/4 lhamas (arredondado para baixo)

Onde n = população atual no ano

Exiba o resultado no formato:
text
Years: n (onde n é o número inteiro de anos calculado)
