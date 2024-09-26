# incease or decrease Value by 1
inpt = int(input().strip())

lines = [input().lower().strip() for _ in range(inpt)]

operation = 0
for i in lines:
    if i == "++x" or i == "x++":
        operation += 1 
    if i == "--x" or i == "x--":
        operation -= 1 
print(operation)
