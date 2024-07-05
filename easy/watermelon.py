melon_kg = int(input().strip())

# Weight in kilo must be greater than 2 and should be even
result = ["YES" if melon_kg > 2 and melon_kg % 2 == 0 else "NO"]
print(result)
