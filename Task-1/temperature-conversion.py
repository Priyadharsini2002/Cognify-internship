def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")

    # Get temperature value and unit from the user
    temperature = float(input("Enter temperature value: "))
    unit = input("Enter unit of measurement (Celsius or Fahrenheit): ").lower()

    # Perform conversion based on the unit entered
    if unit == "celsius":
        converted_temperature = celsius_to_fahrenheit(temperature)
        print(f"{temperature} Celsius is equal to {converted_temperature} Fahrenheit")
    elif unit == "fahrenheit":
        converted_temperature = fahrenheit_to_celsius(temperature)
        print(f"{temperature} Fahrenheit is equal to {converted_temperature} Celsius")
    else:
        print("Invalid unit. Please enter either 'Celsius' or 'Fahrenheit'.")

if __name__ == "__main__":
    main()