#Write your code below this line 👇
def prime_checker(number):
    remain = 0
    span = range(2,number+1)
    not_prime = 0
    for value in span:
        if number % value == 0 and number != value:
            not_prime += 1
        elif number % value > 0:
            remain += number % value
    if remain > 0 and not_prime == 0:
        print("This is a prime number.")
    else:
        print("This is NOT a prime number.")
    

#Write your code above this line 👆
    
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



