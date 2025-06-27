#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool is_valid_key(string key);
void encrypt(string plaintext, string key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    if (!is_valid_key(argv[1]))
    {
        printf("Key must contain 26 unique alphabetic characters.\n");
        return 1;
    }

    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");
    encrypt(plaintext, argv[1]);
    printf("\n");

    return 0;
}

bool is_valid_key(string key)
{
    if (strlen(key) != 26)
    {
        return false;
    }

    int freq[26] = {0};

    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            return false;
        }

        char c = tolower(key[i]);
        freq[c - 'a']++;

        if (freq[c - 'a'] > 1)
        {
            return false;
        }
    }

    return true;
}

void encrypt(string plaintext, string key)
{
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];

        if (isupper(c))
        {
            printf("%c", toupper(key[c - 'A']));
        }
        else if (islower(c))
        {
            printf("%c", tolower(key[c - 'a']));
        }
        else
        {
            printf("%c", c);
        }
    }
}
