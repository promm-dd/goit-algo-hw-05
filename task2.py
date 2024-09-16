import re 
def generator_numbers(text: str):
    numbers = re.findall(r"\b\d+\b.\d+|\d+\b", text)
    for number in numbers:  
        yield float(number) #преобразуем строку в число 
    
    
def sum_profit(text:str, func: callable):
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
