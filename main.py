#Write your code below this line 👇
def prime_checker(number):
    remain = 0
    span = range(2,number+1)

    for value in span:
        if number % value == 0 and number != value:
            print("This is not a prime number.")
            break
        if number % value > 0:
            remain += number % value
        elif remain > 0 and value == number:
            print("This is a prime number")

#Write your code above this line 👆
    
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



