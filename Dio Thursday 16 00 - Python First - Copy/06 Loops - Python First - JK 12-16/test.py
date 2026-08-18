def range_inclusive(start, stop, step=1):
    return range(start, stop + step, step)

# Usage: loops 1 to 10 inclusive
for i in range_inclusive(1, 10):
    print(i)

    