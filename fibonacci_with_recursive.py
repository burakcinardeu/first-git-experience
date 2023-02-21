def fib(x):
    if x>=2:
        toplam = fib(x-1)+fib(x-2)
    else:
        return x
    return toplam 

print(fib(7))