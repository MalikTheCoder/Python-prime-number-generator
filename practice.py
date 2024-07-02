from colorama import Fore, Back, Style
from math import sqrt

#age = 21
#country = "UK"
#if age > 17:
#    print (Fore.GREEN + "Yes I can serve you")
#else:
#    print (Fore.RED + "You aren't old enough")


#password = "CHICKEN"

#if len(password) < 8:
   # print("That password is too short")
#else: 
   # print((password)  + " is accepted")


#num = 30

#if num % 3 or num % 5:
  #  print("This number is divisable by 3 or 5")
#else:
 #   print("This number is not divisable by 3 or 5")

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# while True:
#     # Get user input
#     num = int(input("Enter a number: "))

#     # Check if the number is prime and print the result
#     if is_prime(num):
#         print(Fore.GREEN + f"{num} is a prime number")
#         break
#     else:
#         print(Fore.RED + "This is not a prime number. Try another number.")

    #Wrap while loop in for loop, rather than printing add to an array

    

# Function to check if a number is prime
def is_prime(num):
    if num < 2:  # 
        return False
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:  
            return False
    return True

# Main function to generate prime numbers up to a given limit
def generate_primes(limit):
    primes = []  # List to store prime numbers
    for num in range(2, limit + 1):  
        if is_prime(num):  
            primes.append(num)  
    return primes

# Function to get valid user input
def get_valid_input():
    while True:
        user_input = (input(f"{Fore.BLUE}Enter how many prime numbers you want!!! (up to 10000 please :)): {Fore.GREEN}"))
        if user_input.isnumeric() == False: 
            print("Please enter a number")
        else:
            user_input= int(user_input)
            if user_input <= 0:
                print(Fore.RED + "Please enter a positive integer (you're breaking my code!!).")
            elif user_input > 10000:
                print(Fore.RED + "Please enter a number less than or equal to 10000 (you're breaking my code!!).")
            elif user_input <= 1:
                print(Fore.RED + "Please enter a number above 1 (you're breaking my code!!)")
            else:
                return user_input

# Main script
user_input = get_valid_input()
prime_numbers = generate_primes(user_input)  # Generate prime numbers up to user input
print(f"Prime numbers up to {user_input}: {prime_numbers}")
