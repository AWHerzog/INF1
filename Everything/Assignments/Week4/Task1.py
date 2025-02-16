number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pi = 3.1415 
def square_root_dict(numbers: [int]):
    return {x: x**0.5 for x in numbers}


def even_odd_dict(numbers: [int]):
    return {x: "even" if x % 2 == 0 else "odd" for x in numbers}


def area_dict(numbers: [int]):
    return {x:
    { 
        "square": x**2 ,
        "circle": pi * x ** 2
    } for x in numbers if x > 0}


def smaller_larger_dict(numbers: [int]):
    return {x: 
    {
        f"{i}: larger" if i > x else f"{i}: smaller" for i in numbers if i!=x
    } for x in numbers}



print(area_dict(number_list))
