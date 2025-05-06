import os

def get_local_path(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def sort_and_filter_scores():
    try:
        file_name = input("Enter the name of the file with results (e.g., scores.txt): ")
        file_path = get_local_path(file_name)

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        participants = []
        for line in lines:
            try:
                parts = line.strip().split()
                if len(parts) < 2:
                    raise ValueError
                name = parts[0]
                score = int(parts[1])
                participants.append((name, score))
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

        result_path = get_local_path('res.txt')
        with open(result_path, 'w', encoding='utf-8') as f:
            for p in filtered_participants:
                f.write(f"{p[0]} {p[1]}\n")
        print(f"Participants with a score above {N} written to 'res.txt'.")
    
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid data format or input.")

sort_and_filter_scores()
