from cs50 import get_int

def main():
    # Solicitar altura válida (1-8)
    while True:
        height = get_int("Height: ")
        if height is not None and 1 <= height <= 8:
            break

    # Imprimir as duas pirâmides
    for i in range(1, height + 1):
        # Espaços antes da primeira pirâmide
        print(" " * (height - i), end="")
        # Primeira pirâmide
        print("#" * i, end="")
        # Espaço entre as pirâmides (2 espaços)
        print("  ", end="")
        # Segunda pirâmide
        print("#" * i)

if __name__ == "__main__":
    main()
