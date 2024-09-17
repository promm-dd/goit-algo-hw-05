def caching_fibonacci():
    fib_cache={}
    def fibonacci(n):
        if n in fib_cache: # если  n  в кеше, то возвращаем значение фиб
            return fib_cache[n] #сохран результат в кеше 
        
        if n <= 0: #базовое значение фиб  
            fib_cache[n]= n
            return fib_cache[n] 
        elif n == 1:
            fib_cache[n]= n
            return fib_cache[n]
        else:
            fib_cache[n]= fibonacci(n-1) + fibonacci(n-2)
            return fib_cache[n]
    return fibonacci #возвр внутренню функцию  без вызова

fib= caching_fibonacci() #создаем функц фибон с кешированием
print(fib(10))
print(fib(15))

    
    
    
    
    
    
    
    

    

# def fibonacci(n):
#     a,b = 0, 1
#     for _ in range(n):
#         a, b = b, a+b
#     return a # Возвращаем n-е число Фибоначчи
# print(fibonacci(6))
# print(fibonacci(10))


# fib_cache= {}
# def fibonacciization(n):
#     if n in fib_cache:
#         return fib_cache[n]  # Если n уже в кэше, возвращаем сохраненное значение
#     if n <=1:
#         fib_cache[n] = n # Сохраняем результат для F(0) и F(1) в кэше
#     else:
#         fib_cache[n]= fibonacciization(n-1) + fibonacciization(n-2)
#     return fib_cache[n]
    
# print(fibonacciization(5))   


# def fibonacci_generator():
#     a, b= 0,1
#     while True:
#         yield a# Генерируем текущее значение a
#         a, b = b, a+b
        
# gen = fibonacci_generator()
# for _ in range(6):
#     print(next(gen))
