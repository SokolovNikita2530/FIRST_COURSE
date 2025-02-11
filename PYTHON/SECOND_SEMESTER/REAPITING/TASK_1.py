import datetime

def calculate_days():
    try:
        birth_date_str = input("Enter your birth date in the format YYYY-MM-DD: ")
        birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        today = datetime.date.today()
        days_difference = (today - birth_date).days
        print(f"Days passed since your birth: {days_difference}")
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")
    
calculate_days()
