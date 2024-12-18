import math
def zoo(number):
    # return a tuple containing the required values
   
    return math.floor(number), math.ceil(number), math.atan(number), math.modf(number), math.nextafter((number), -math.inf), math.cbrt(number)

   

print(zoo(100))