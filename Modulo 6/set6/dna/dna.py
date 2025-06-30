import csv
import sys

def main():
    # Verificar argumentos da linha de comando
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Carregar o banco de dados CSV
    database = []
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)

    # Carregar a sequência de DNA
    with open(sys.argv[2], 'r') as file:
        sequence = file.read().strip()

    # Obter a lista de STRs a serem verificados
    strs = list(database[0].keys())[1:]

    # Calcular as contagens máximas de STRs
    str_counts = {}
    for str_seq in strs:
        str_counts[str_seq] = longest_match(sequence, str_seq)

    # Verificar correspondência no banco de dados
    match = find_match(database, str_counts)
    print(match if match else "No match")

def longest_match(sequence, subsequence):
    """Retorna o número máximo de repetições consecutivas de subsequence em sequence"""
    max_count = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if end > sequence_length:
                break
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        if count > max_count:
            max_count = count

    return max_count

def find_match(database, str_counts):
    """Encontra a pessoa no banco de dados com contagens de STR correspondentes"""
    for person in database:
        match = True
        for str_seq in str_counts:
            if int(person[str_seq]) != str_counts[str_seq]:
                match = False
                break
        if match:
            return person['name']
    return None

if __name__ == "__main__":
    main()
