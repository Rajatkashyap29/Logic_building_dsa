def CheckPrime(num:int):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        else:
            return True
    i+=1

print(CheckPrime(1))    

