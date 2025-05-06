import os

def get_local_path(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def generate_ngrams():
    try:
        file_name = input("Enter the name of the text file (e.g., text.txt): ")
        file_path = get_local_path(file_name)

        N = int(input("Enter value N for N-grams: "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        words = text.split()
        if len(words) < N:
            print("Not enough words to generate N-grams.")
            return

        ngrams = [words[i:i+N] for i in range(len(words) - N + 1)]
        
        print(f"\n{N}-grams:")
        for ngram in ngrams:
            print(" ".join(ngram))

    except FileNotFoundError:
        print("File not found.")
    except ValueError as e:
        print(f"Invalid input: {e}")

generate_ngrams()
