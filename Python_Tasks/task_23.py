import random

target_number = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Enter your guess between 1 and 100: "))
    attempts += 1
    if guess == target_number:
        print(
            f"Congratulations !!You guessed the correct number {target_number} in {attempts} attempts."
        )
        break
    elif guess > target_number:
        print("Too high Try going Lower.")
    else:
        print("Too Low Try going Higher.")
