from datetime import datetime

# Checking if the data exists and follows the correct format
def validate_date(input_date):
    try:
        # Try to parse the input date
        birth_date = datetime.strptime(input_date, "%m/%d/%Y")
        return birth_date
    except ValueError:
        return None

# Calculating the age from the input date to current date
def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year

    # Adjust age if the birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

# The main function which will call the above functions 
def main():
    user_input = input("Enter your birth date (mm/dd/yyyy): ")
    birth_date = validate_date(user_input)

    if birth_date is None: ## To handle invaild inputs 
        print("Invalid date format or non-existent date. Please use mm/dd/yyyy.")
        return

    age = calculate_age(birth_date)
    european_format = birth_date.strftime("%d/%m/%Y")

    print(f"\nYour current age is: {age} years")
    print(f"Your birth date in European format is: {european_format}")

# Run the program
if __name__ == "__main__":
    main()

