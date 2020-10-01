#Ciag Fibonacciego
# Suma dwóch poprzednich wyrazów tego ciagu
# 1,1,2,3,5,8,13

def fin(n):
    if n==1:
        return 1

    if n==2:
        return 1
    
    if n > 2:
        return fin(n -1) + fin(n -2)


print(fin(1))
print(fin(2))
print(fin(3))
print(fin(4))
print(fin(5))
print(fin(6))
print(fin(7))