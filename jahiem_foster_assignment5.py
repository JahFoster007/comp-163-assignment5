# TEST CASE 1: Collatz Conjecture
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", current_number, end=" ")
while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = (current_number * 3) + 1
    print(current_number, end=" ")
    step_count = step_count + 1

print()
print(f"Steps: {step_count}")

# TEST CASE 2: Prime Number Checker
print("=== Challenge 2: Prime Number Checker ===")
num = int(input("Enter a number: "))

if num > 1: # No negative values are needed for this test case
    print(f"Testing divisors from 2 to {num - 1}...")
    for i in range(2, num):
        if num % i == 0: # If the remainder is equal to 0, it's not prime.
            print(f"{num} is not prime (divisible by {i})")
            break
    else:
        print(f"{num} is prime!")
else:
    print(f"{num} is not prime")

print()