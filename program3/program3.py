# Menu Display
print("=============================")
print("   UNIT & CURRENCY CONVERTER")
print("=============================")
print("1. Celsius to Fahrenheit")
print("2. Km to Miles")
print("3. INR to USD")
print("4. Fahrenheit to Celsius")
print("5. Miles to Km")
print("6. USD to INR")
print("=============================")

# Input menu choice
choice = int(input("Enter choice: "))

# Fixed conversion rate (1 USD = 83.5 INR)
INR_TO_USD_RATE = 83.5

result = 0.0

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    result = (celsius * 9/5) + 32
    print(f"\n{celsius}°C = {round(result, 2)}°F")

elif choice == 2:
    km = float(input("Enter distance in Km: "))
    result = km * 0.621371
    print(f"\n{km} Km = {round(result, 2)} Miles")

elif choice == 3:
    inr = float(input("Enter amount in INR: "))
    result = inr / INR_TO_USD_RATE
    print(f"\n{inr} INR = {round(result, 2)} USD")

elif choice == 4:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    result = (fahrenheit - 32) * 5/9
    print(f"\n{fahrenheit}°F = {round(result, 2)}°C")

elif choice == 5:
    miles = float(input("Enter distance in Miles: "))
    result = miles / 0.621371
    print(f"\n{miles} Miles = {round(result, 2)} Km")

elif choice == 6:
    usd = float(input("Enter amount in USD: "))
    result = usd * INR_TO_USD_RATE
    print(f"\n{usd} USD = {round(result, 2)} INR")

else:
    print("\nInvalid choice! Please select 1 to 6.")

# Memory id and type of result variable
if 1 <= choice <= 6:
    print(f"Memory id of result variable: {id(result)}")
    print(f"Result type: {type(result)}")