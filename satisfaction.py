import itertools

variables = ["A", "B", "C", "D"]

colors = ["Red", "Blue", "Yellow"]

all_assignments = itertools.product(colors, repeat=len(variables))

def valid(i):
    A, B, C, D = i
    return (A != B) and (B != C) and (A != C) and (A != D) and (B != D) and (C != D)

solutions = []

for i in all_assignments:
    if valid(i):
        solutions.append(dict(zip(variables, i)))

print("Valid colorings of the map:")

for sol in solutions:
    print(sol)

#return (A != B) and (B != C) and (A != C)

