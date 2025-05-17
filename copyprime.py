'''Write the definition of a method/function Copy_Prime(lst) to copy all the
prime numbers from the list lst to another list lst_prime.'''


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def copy_prime(lst):
    lst_prime=[]
    for prime in lst:
        if (is_prime(prime)):
            lst_prime.append(prime)
    return lst_prime
            
    

numbers=[1,2,3,4,5,6,7]

print("The original list is: \n", numbers)
print("The list of prime numbers is :")
print(copy_prime(numbers))


