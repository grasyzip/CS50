# CS50 - O Curso de Ciência da Computação de Harvard no Brasil

Esse é o curso introdutório de Ciência da Computação de Harvard, um dos cursos mais conhecidos mundialmente. Os alunos aprendem os conteúdos fundamentais sobre como computadores e a Internet funcionam, garantindo uma ótima base para aprofundar seus estudos em Web Design, Bancos de Dados, Sistemas Eletrônicos, Desenvolvimento de Software, entre outros.

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

## Modulo 2: Arrays Exercicios:

### 1. Scrabble
Seu programa deve solicitar entrada duas vezes: uma vez para que "Jogador 1" insira sua palavra e outra vez para que "Jogador 2" insira sua palavra. Em seguida, dependendo de qual jogador marcar mais pontos, seu programa deve imprimir “Player 1 wins!” (caso o jogador 1 ganhe), “Player 2 wins!” (se o jogador 2 venceu) ou “Tie!” (caso os dois jogadores pontuem igualmente).

1. Pseudocódigo
Se ainda não tiver certeza de como resolver o problema em si, divida-o em problemas menores que você provavelmente pode resolver primeiro. Por exemplo, este exercício se divide em:

- Solicitar ao usuário duas palavras;
- Calcular os pontos de cada palavra;
- Imprimir o vencedor.

### 2. Legibilidade
Vamos escrever um programa chamado readability que recebe um texto e determina seu nível de leitura. 
O texto que o usuário inseriu tem 65 letras, 4 sentenças e 14 palavras. 65 letras por 14 palavras é uma média de cerca de 464,29 letras por 100 palavras. E 4 sentenças por 14 palavras é uma média de cerca de 28,57 sentenças por 100 palavras. Conectados à fórmula Coleman-Liau e arredondados para o número inteiro mais próximo, obtemos uma resposta de 3: portanto, esta passagem está em um nível de leitura da terceira série.

### 3. Caesar

Vamos escrever um programa chamado ceasar.c que permite criptografar mensagens usando a cifra de César. No momento em que o usuário executa o programa, ele deve decidir, fornecendo um argumento de linha de comando, qual deve ser a chave na mensagem secreta que fornecerá no tempo de execução. Não devemos necessariamente presumir que a chave do usuário será um número; embora você possa assumir que, se for um número, será um inteiro positivo.

### 4. Substituição

Projete e implemente um programa, substitution, que criptografa mensagens usando uma cifra de substituição.
Implemente seu programa em um arquivo denominado substitution.c em um diretório denominado pset2/substitution.

- Seu programa deve aceitar um único argumento de linha de comando, a chave a ser usada para a substituição. A chave em si não deve fazer distinção entre maiúsculas e minúsculas, portanto, se algum caractere na chave estiver em maiúscula ou minúscula, isso não deve afetar o comportamento do seu programa.
- Se o seu programa for executado sem nenhum argumento de linha de comando ou com mais de um argumento de linha de comando, seu programa deve imprimir uma mensagem de erro de sua escolha (com printf) e retornar de main um valor de 1 (o que tende a significar um erro) imediatamente.
- Se a chave for inválida (por não conter 26 caracteres, conter qualquer caractere que não seja um caractere alfabético, ou não conter cada letra exatamente uma vez), seu programa deverá imprimir uma mensagem de erro de sua escolha (com printf) e retornar do main um valor de 1 imediatamente.
- Seu programa deve produzir na saída plaintext: - que significa texto simples: (sem uma nova linha) e então solicitar ao usuário uma string de texto simples (usando get_string).
- Seu programa ter na saída o seguinte texto ciphertext: - que significa texto cifrado - (sem uma nova linha) seguido pelo texto cifrado correspondente do texto simples, com cada caractere alfabético no texto simples substituído pelo caractere correspondente no texto cifrado; os caracteres não alfabéticos devem ser reproduzidos inalterados.
- Seu programa deve preservar maiúsculas e minúsculas: as letras maiúsculas devem permanecer letras maiúsculas; as letras minúsculas devem permanecer em minúsculas.
- Após a saída do texto cifrado, você deve imprimir uma nova linha. Seu programa deve então sair retornando 0 da main.

