## Checking if the input is a prime num
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True 

## Checking if the input is a positive num (all nums above 0) 
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a **positive** integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid **integer**.")

# The main function  
def main():
    print("Prime Number Generator")

    start = get_positive_integer("Enter the start of the range: ") ## Starting from
    end = get_positive_integer("Enter the end of the range: ") ## Ending at 
    
    ## To handle invaild input 
    if start > end: 
        print("Start of range must be less than or equal to end of range.")
        return
    # Checks if num is prime 
    # If prime add to the list and moves to the next num
    # using for loop 
    primes = [num for num in range(start, end + 1) if is_prime(num)]

    if not primes:
        print("No prime numbers found in the given range.")
        return

    print("\nPrime numbers between", start, "and", end, ":")
    for i, prime in enumerate(primes, 1):
        print(f"{prime:4}", end='\n' if i % 10 == 0 else ' ')
    print()

if __name__ == "__main__":
    main()
