import datetime

def calculate_days():
    try:
        birth_date_str = input("Enter your birth date in the format DD.MM.YYYY: ")
        birth_date = datetime.datetime.strptime(birth_date_str, "%d.%m.%Y").date()
        today = datetime.date.today()
        days_difference = (today - birth_date).days
        print(f"Days passed since your birth: {days_difference}")
    except ValueError:
        print("Invalid date format. Please use the format DD.MM.YYYY.")
    
calculate_days()
