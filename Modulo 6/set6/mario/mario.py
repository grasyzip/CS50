from cs50 import get_int

def main():
    while True:
        height = get_int("Height: ")
        if height is not None and 1 <= height <= 8:
            break

    for i in range(1, height + 1):
        print(" " * (height - i), end="")
        print("#" * i)

if __name__ == "__main__":
    main()
