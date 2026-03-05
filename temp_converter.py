def convert_temp(celsius: float) -> float:
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    temp_celsius = float(input("Enter temperature in Celsius: "))

    temp_fahrenheit = convert_temp(temp_celsius)

    if temp_fahrenheit > 0:
        print(f"{temp_celsius} C is {temp_fahrenheit} F")
    else:
        print(f"{temp_celsius} C is {temp_fahrenheit} F")

if __name__ == "__main__":
    main()