import asyncio

async def print_numbers():
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)

# Run the coroutine
asyncio.run(print_numbers())


results = [35, 55, 78, 92, 48, 81, 67, 89, 50]

# Keep passing scores: >= 50
passed = list(filter(lambda s: s >= 50, results))

# Convert to letter grades
grades = list(map(lambda score:
                  'A' if score >= 90 else
                  'B' if score >= 80 else
                  'C' if score >= 70 else
                  'D' if score >= 60 else
                  'E',
                  passed))

print(grades)


