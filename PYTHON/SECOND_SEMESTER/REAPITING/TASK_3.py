def sort_and_filter_scores():
    try:
        file_path = input("Enter the path to the file with results: ")
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        participants = []
        for line in lines:
            try:
                name, score = line.split()
                participants.append((name, int(score)))
            except ValueError:
                print(f"Error in line: {line.strip()}")
        
        participants_sorted_by_name = sorted(participants, key=lambda x: x[0])
        print("Sorted by name:")
        for p in participants_sorted_by_name:
            print(f"{p[0]} {p[1]}")

        participants_sorted_by_score = sorted(participants, key=lambda x: x[1], reverse=True)
        print("\nSorted by score:")
        for p in participants_sorted_by_score:
            print(f"{p[0]} {p[1]}")

        N = int(input("Enter value N for filtering: "))
        filtered_participants = [p for p in participants if p[1] > N]
        
        with open('res.txt', 'w', encoding='utf-8') as f:
            for p in filtered_participants:
                f.write(f"{p[0]} {p[1]}\n")
        print(f"Participants with a score above {N} written to 'res.txt'.")
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid data format in the file.")
    
sort_and_filter_scores()
