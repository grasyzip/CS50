#include <cs50.h>
#include <math.h>
#include <stdio.h>

// valida cartão usando algoritmo de Luhn
bool validate_card(long numero);

// calcula quantidade de dígitos no cartão
int get_card_length(long numero);

// identifica a bandeira (AMEX, VISA, etc.)
string identify_issuer(long numero, int comprimento);

int main(void)
{
    // armazena o número do cartão (long para números grandes)
    long numero;

    // solicita número do cartão até receber um número positivo válido
    do
    {
        numero = get_long("Número: ");
    }
    while (numero < 1);  // rejeita números negativos e zero

    // obtém o comprimento (quantidade de dígitos) do número do cartão
    int comprimento = get_card_length(numero);

    // primeira validação: Verifica se passa no algoritmo de Luhn
    if (!validate_card(numero))
    {
        printf("INVALID\n");
        return 0;  // encerra se o cartão for inválido
    }

    // se o cartão for válido, identifica a bandeira
    string bandeira = identify_issuer(numero, comprimento);
    printf("%s\n", bandeira);
    // imprime a bandeira (AMEX, MASTERCARD, VISA) ou INVALID

    return 0; // encerramento bem-sucedido do programa
}

/*
 * Valida número do cartão usando algoritmo de Luhn
 * @param numero O número do cartão de crédito para validação
 * @return true se válido, false se inválido
 */
bool validate_card(long numero)
{
    int soma = 0;          // Armazenará a soma para verificação de Luhn
    bool alternar = false; // Flag para alternar entre dígitos pares e ímpares
    long temp = numero;    // Variável temporária para processamento

    // processa cada dígito do número
    while (temp > 0)
    {
        int digito = temp % 10;  // extrai o último dígito

        // para cada segundo dígito (começa pelo penúltimo)
        if (alternar)
        {
            digito *= 2;  // multiplica o dígito por 2
            // soma os dígitos do produto (ex: 16 vira 1 + 6)
            soma += (digito / 10) + (digito % 10);
        }
        else
        {
            soma += digito;  // soma o dígito diretamente
        }

        alternar = !alternar;  // alterna o flag
        temp /= 10;           // remove o último dígito
    }

    // cartão é válido se a soma for múltiplo de 10
    return (soma % 10 == 0);
}

/*
 * calcula a quantidade de dígitos no número do cartão
 * @param numero O número do cartão de crédito
 * @return Quantidade de dígitos no cartão
 */

int get_card_length(long numero)
{
    int comprimento = 0;

    // conta dígitos dividindo repetidamente por 10
    while (numero > 0)
    {
        numero /= 10;
        comprimento++;
    }
    return comprimento;
}

/*
 * identifica a bandeira do cartão baseado em padrões numéricos
 * @param numero O número do cartão de crédito
 * @param comprimento Quantidade de dígitos no cartão
 * @return Nome da bandeira como string (AMEX, MASTERCARD, VISA) ou INVALID
 */
string identify_issuer(long numero, int comprimento)
{
    // extrai os dois primeiros dígitos do cartão
    int primeiros_dois = numero / pow(10, comprimento - 2);

    // extrai apenas o primeiro dígito
    int primeiro = primeiros_dois / 10;

    // verificação American Express:
    // 15 dígitos, começa com 34 ou 37
    if (comprimento == 15 && (primeiros_dois == 34 || primeiros_dois == 37))
        return "AMEX";

    // verificação Mastercard:
    // 16 dígitos, começa com 51-55
    else if (comprimento == 16 && (primeiros_dois >= 51 && primeiros_dois <= 55))
        return "MASTERCARD";

    // verificação Visa:
    // 13 ou 16 dígitos, começa com 4
    else if ((comprimento == 13 || comprimento == 16) && primeiro == 4)
        return "VISA";

    // se nenhum dos padrões acima corresponder
    else
        return "INVALID";
}

/*int main(void)
{
    long numero;
    do
    {
        numero = get_long("Número: ");
    }
    while (numero < 1);

    // verifica o comprimento e bandeira
    int comprimento = 0;
    long temp = numero;
    while (temp > 0)
    {
        temp /= 10;
        comprimento++;
    }

    // verifica se comprimento é válido
    if (comprimento != 13 && comprimento != 15 && comprimento != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    // aplica algoritmo de Luhn
    int soma = 0;
    temp = numero;
    for (int i = 1; i <= comprimento; i++)
    {
        int digito = temp % 10;

        if (i % 2 == 0)
        {
            digito *= 2;
            soma += (digito / 10) + (digito % 10);
        }
        else
        {
            soma += digito;
        }

        temp /= 10;
    }

    // verifica validade do número
    if (soma % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // identifica a bandeira
    int primeirosDigitos = numero / pow(10, comprimento - 2);

    if ((comprimento == 15) && (primeirosDigitos == 34 || primeirosDigitos == 37))
    {
        printf("AMEX\n");
    }
    else if ((comprimento == 16) && (primeirosDigitos >= 51 && primeirosDigitos <= 55))
    {
        printf("MASTERCARD\n");
    }
    else if ((comprimento == 13 || comprimento == 16) && (primeirosDigitos / 10 == 4))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}*/
