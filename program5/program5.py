# ==========================================
# PART A: Simple & Compound Interest Calculator
# ==========================================
print("--- Interest Calculator ---")

# Inputs and type casting
principal = float(input("Principal: "))
rate = float(input("Rate (%): "))
time = float(input("Time (years): "))

# Type confirmation checks
print(f"\nDatatype of Principal: {type(principal)}")
print(f"Datatype of Rate: {type(rate)}")
print(f"Datatype of Time: {type(time)}")

# Calculations
si = (principal * rate * time) / 100
ci = principal * ((1 + rate / 100) ** time) - principal

print(f"\nSimple Interest = Rs. {round(si, 2)}")
print(f"Compound Interest = Rs. {round(ci, 2)}")
print(f"Difference (CI - SI) = Rs. {round(ci - si, 2)}\n")


# ==========================================
# PART B: Age Calculator
# ==========================================
print("--- Age Calculator ---")

CURRENT_YEAR = 2026

# Input and type casting
birth_year = int(input("Enter your birth year: "))

# Type confirmation check
print(f"Datatype of Birth Year: {type(birth_year)}")

# Calculation
age = CURRENT_YEAR - birth_year

print(f"\nYour age in {CURRENT_YEAR} is: {age} years")