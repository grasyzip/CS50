from cs50 import get_float

def main():
    # Solicitar valor do troco até obter um valor não negativo
    while True:
        change = get_float("Change owed: ")
        if change is not None and change >= 0:
            break

    # Converter dólares para centavos e arredondar para evitar erros de ponto flutuante
    cents = round(change * 100)

    # Inicializar contador de moedas
    coins = 0

    # Valores das moedas em centavos
    denominations = [25, 10, 5, 1]

    # Calcular número mínimo de moedas
    for denom in denominations:
        coins += cents // denom
        cents %= denom
        if cents == 0:
            break

    # Imprimir o resultado
    print(coins)

if __name__ == "__main__":
    main()
