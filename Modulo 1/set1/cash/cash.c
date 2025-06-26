#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    float reais;
    int centavos;

    // solicita valor válido (positivo)
    do
    {
        reais = get_float("Troca devida: ");
    }
    while (reais < 0);

    // converte reais para centavos e arredonda
    centavos = round(reais * 100);

    // calcula moedas necessárias
    int moedas = 0;
    int valores[] = {25, 10, 5, 1};
    int tamanho = sizeof(valores) / sizeof(valores[0]);

    for (int i = 0; i < tamanho; i++)
    {
        moedas += centavos / valores[i];
        centavos %= valores[i];
    }

    // imprimi resultado
    printf("%d\n", moedas);
}
