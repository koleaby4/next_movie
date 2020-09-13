import random

if __name__ == "__main__":
    for _ in range(100):
        first = random.choice([10, 100, 1000, 10000, 1000000])
        second = random.choice([10, 100, 1000])
        nr = round(random.random() * first, 4)
        print(f"{nr:,} * {second:,} = ")
