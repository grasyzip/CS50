from cs50 import get_string
import re

def main():
    # Solicitar texto ao usuário
    text = get_string("Text: ")

    # Contar letras, palavras e frases
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calcular médias por 100 palavras
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Calcular índice Coleman-Liau
    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)

    # Determinar o nível de legibilidade
    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")

def count_letters(text):
    """Conta o número de letras no texto (a-z, A-Z)"""
    return len(re.findall(r'[a-zA-Z]', text))

def count_words(text):
    """Conta o número de palavras no texto (separadas por espaços)"""
    # Remove espaços extras e divide por espaços
    return len(text.strip().split())

def count_sentences(text):
    """Conta o número de frases no texto (terminadas por . ! ?)"""
    return len(re.findall(r'[.!?]', text))

if __name__ == "__main__":
    main()
