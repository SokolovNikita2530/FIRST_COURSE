import random

def get_user_choice():
    while True:
        try:
            choice = int(input("Сколько камней вы хотите взять (1, 2 или 3)? "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Пожалуйста, выберите 1, 2 или 3.")
        except ValueError:
            print("Введите число.")

def computer_choice(remaining):
    # Логика для того, чтобы оставить сопернику 1 камень
    if remaining > 4:
        # Если оставшихся камней больше 4, выбираем так, чтобы оставить 1
        return (remaining - 1) % 4 or 1  # Оставляем сопернику 1 камень
    else:
        # Если осталось 4 или меньше, забираем все, кроме 1
        return remaining - 1

def play_game():
    N = random.randint(4, 30)
    n = N
    print("-----------------------------")

    while N > 0:
        if n == N:
            print(f"Начинаем игру с {N} камнями.")
        else:
            print(f"Осталось камней: {N}")
        
        # Ход игрока
        user_take = get_user_choice()
        N -= user_take
        if N <= 0:
            print("Вы забрали последние камни. Компьютер победил!")
            break

        print("-----------------------------")

        # Ход компьютера
        computer_take = computer_choice(N)
        N -= computer_take
        print(f"Компьютер взял {computer_take} камня(ей).")

        if N <= 0:
            print("Компьютер забрал последние камни. Вы победили!")
            break
        
        print("-----------------------------")

if __name__ == "__main__":
    play_game()
