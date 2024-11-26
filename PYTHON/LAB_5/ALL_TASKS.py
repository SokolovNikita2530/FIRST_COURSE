import random
import sys

def get_user_choice():
    """Запрашивает у пользователя количество камней для взятия (1, 2 или 3) и проверяет ввод."""
    while True:
        user_input = input("Сколько камней вы хотите взять (1, 2 или 3)?: ")
        if user_input.upper() == 'Q':
            sys.exit("Вы вышли из игры.")
        try:
            choice = int(user_input)
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Пожалуйста, выберите 1, 2 или 3.")
        except ValueError:
            print("Ошибка: введите число.")

def computer_choice(remaining):
    """Определяет, сколько камней возьмет компьютер, основываясь на количестве оставшихся камней."""
    if remaining > 8:
        return random.randint(1, 3)
    elif remaining > 4:
        return remaining - 5
    else:
        if remaining - 1 == 0:
            return 1 
        else: return remaining - 1

def display_remaining_stones(remaining):
    """Выводит количество оставшихся камней."""
    print(f"Осталось камней: {remaining}")

def play_game():
    """Основная функция для управления игровым процессом."""
    N = random.randint(4, 31)
    print("Игра началась! Для выхода введите Q.")
    print("-----------------------------")
    print(f"Начинаем игру с {N} камнями.")
    
    while N > 0:
        # Ход игрока
        user_take = get_user_choice()
        N -= user_take
        
        if N <= 0:
            print("Вы забрали последние камни. Компьютер победил!")
            break
        
        display_remaining_stones(N)
        print("-----------------------------")

        # Ход компьютера
        computer_take = computer_choice(N)
        N -= computer_take
        print(f"Компьютер взял {computer_take} камня(ей).")

        if N <= 0:
            print("Компьютер забрал последние камни. Вы победили!")
            break
        
        display_remaining_stones(N)
        print("-----------------------------")

if __name__ == "__main__":
    play_game()
