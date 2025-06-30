from cs50 import get_string

def main():
    # Solicitar número do cartão
    while True:
        number = get_string("Number: ")
        if number.isdigit():
            break

    # Verificar validade usando algoritmo de Luhn
    if not luhn_valid(number):
        print("INVALID")
        return

    # Identificar o tipo de cartão
    length = len(number)

    if length == 15 and (number.startswith('34') or number.startswith('37')):
        print("AMEX")
    elif length == 16 and number.startswith(('51', '52', '53', '54', '55')):
        print("MASTERCARD")
    elif (length == 13 or length == 16) and number.startswith('4'):
        print("VISA")
    else:
        print("INVALID")

def luhn_valid(number):
    """Implementação do algoritmo de Luhn"""
    total = 0
    # Iterar sobre os dígitos da direita para a esquerda
    for i, digit in enumerate(reversed(number)):
        n = int(digit)
        # Dígitos em posições pares (considerando 0-based)
        if i % 2 == 1:
            n *= 2
            # Somar dígitos se o resultado for maior que 9
            total += n if n < 10 else (n // 10) + (n % 10)
        else:
            total += n
    return total % 10 == 0

if __name__ == "__main__":
    main()
