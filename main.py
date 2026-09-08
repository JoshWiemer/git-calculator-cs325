import random

def generate_numbers(count=10, minimum=1, maximum=100):
    """Generate a list of random integers."""
    return [random.randint(minimum, maximum) for _ in range(count)]

def main():
    print("Random Integer Generator")
    print("-" * 25)

    numbers = generate_numbers()
    print("Generated numbers:", numbers)
    print("Smallest:", min(numbers))
    print("Largest:", max(numbers))
    print("Average:", sum(numbers) / len(numbers))

if __name__ == "__main__":
    main()