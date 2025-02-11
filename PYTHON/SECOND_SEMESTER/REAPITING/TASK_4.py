def generate_ngrams():
    try:
        file_path = input("Enter the path to the text file: ")
        N = int(input("Enter value N for N-grams: "))
        
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        words = text.split()
        if len(words) < N:
            print("Not enough words to generate N-grams.")
            return

        ngrams = [words[i:i+N] for i in range(len(words) - N + 1)]
        
        print(f"{N}-grams:")
        for ngram in ngrams:
            print(" ".join(ngram))

    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid data format.")
    
generate_ngrams()
