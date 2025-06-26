#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int inicio, fim, anos = 0;

    // Solicitar tamanho inicial (mínimo 9)
    do
    {
        inicio = get_int("Start size: ");
    }
    while (inicio < 9);

    // Solicitar tamanho final (deve ser ≥ tamanho inicial)
    do
    {
        fim = get_int("End size: ");
    }
    while (fim < inicio);

    // Calcular anos necessários para crescimento
    int populacao = inicio;
    while (populacao < fim)
    {
        // A cada ano: nascimentos = populacao/3, mortes = populacao/4
        populacao += (populacao / 3) - (populacao / 4);
        anos++;
    }

    // Imprimir resultado
    printf("Years: %i\n", anos);

    return 0;
}
