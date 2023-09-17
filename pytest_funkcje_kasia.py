import math

def dodawanie(a, b):
    return a + b

def mnozenie(a, b):
    return round(a * b, 10)

def fizzbuzz(i):
    try:
        float(i)
        i = math.floor(i)
        if i > 0:
            if i%3 != 0 and i%5 != 0:
                return i
            elif i%3 == 0 and i%5 != 0:
                return "fizz"
            elif i%5 == 0 and i%3 != 0:
                return "buzz"
            if i%5 == 0 and i%3 == 0:
                return "fizzbuzz"
        elif i <= 0:
            return None
    except:
        return None
