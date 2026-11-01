# You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

# Return the array ans. Answers within 10-5 of the actual answer will be accepted.

# Note that:

# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius * 1.80 + 32.00

def convertTemperature(celsius: float)->list[float]:
    result = []
    kelvin = celsius + 273.15
    Fahrenheit = celsius * 1.80 + 32.00
    result.append(kelvin)
    result.append(Fahrenheit)
    return result

print(convertTemperature(36.50))