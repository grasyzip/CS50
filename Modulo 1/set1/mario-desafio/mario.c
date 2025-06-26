#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int altura;

    // solicita altura válida (1-8)
    do
    {
        altura = get_int("Altura: ");
    }
    while (altura < 1 || altura > 8);

    // constroe as pirâmides
    for (int i = 0; i < altura; i++)
    {
        // espaços antes da primeira pirâmide
        for (int j = 0; j < altura - i - 1; j++)
        {
            printf(" ");
        }

        // primeira pirâmide
        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }

        // espaço entre as pirâmides (sempre 2)
        printf("  ");

        // segunda pirâmide
        for (int l = 0; l <= i; l++)
        {
            printf("#");
        }

        printf("\n");
    }
}
