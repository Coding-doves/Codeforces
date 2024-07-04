melon_kg = int(input().strip())

# Weight in kilo must be greater than 2 and should be even
if melon_kg > 2 and melon_kg % 2 == 0:
    print("YES")
else:
    print("NO")
