def is_prime(num):
    for div in range(2,num):
        if num % div == 0:
            return False
    return True        

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
