line_nums = int(input().strip())

lines = [input().strip() for _ in range(line_nums)]

problem_solution = 0
for l in lines:
    coun = l.strip().count("1")
    if coun >= 2 and coun <= 3:
        problem_solution += 1
print(problem_solution)
