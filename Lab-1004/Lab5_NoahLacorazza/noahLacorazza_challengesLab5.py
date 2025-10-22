# Challenge 1
CONVERSION_FACTOR = 0.6214
INCREMENTS = list(range(0, 131, 10))

result = []

for i in range(len(INCREMENTS)):
    result.append(INCREMENTS[i] * CONVERSION_FACTOR)

print("""KPH   |   MPH
----------------""")
for i in range(len(result)):
    print(f"{INCREMENTS[i]:5} | {result[i]:.2f}")