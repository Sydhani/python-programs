min=input("Enter the starting value")
max=input("Enter the limit")
number_list = range(min,max)
prime_number = list(filter(lambda x:all(x % y != 0 for y in range(2, x)), number_list))
print(prime_number)




# Prime number is number not divisible by 2, 3 , 5 , 7 for this problem.
