#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Uso: ./recover imagem\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Não foi possível abrir o arquivo %s.\n", argv[1]);
        return 1;
    }

    BYTE buffer[512];
    int jpeg_count = 0;
    FILE *output = NULL;
    char filename[8];

    while (fread(buffer, sizeof(BYTE), 512, input) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (output != NULL)
            {
                fclose(output);
            }

            sprintf(filename, "%03d.jpg", jpeg_count);
            output = fopen(filename, "w");
            if (output == NULL)
            {
                fclose(input);
                printf("Não foi possível criar o arquivo JPEG.\n");
                return 1;
            }

            jpeg_count++;
        }

        if (output != NULL)
        {
            fwrite(buffer, sizeof(BYTE), 512, output);
        }
    }

    if (output != NULL)
    {
        fclose(output);
    }
    fclose(input);

    return 0;
}
