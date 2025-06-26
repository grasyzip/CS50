#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int altura;

    //solicita altura válida (1-8)
    do
    {
        altura = get_int("Altura da pirâmide ( entre 1 e 8): ");
    }
    while (altura < 1 || altura > 8);

    //iterar para cada linha da pirâmide
    for (int i = 0; i < altura; i++)
    {
        //imprimir espaços antes dos #
        for (int j = 0; j < altura - i - 1; j++)
        {
            printf(" ");
        }

        //imprimir os #
        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }

        printf("\n");
    }
}
