# Number-Guessing-Game-in-python
import random

def get_int(prompt, min_val=None, max_val=None):
    """Safely get an integer from the user, enforcing optional bounds."""
    while True:
        val = input(prompt).strip()
        if val.startswith(("+", "-")) and val[1:].isdigit() or val.isdigit():
            num = int(val)
            if (min_val is None or num >= min_val) and (max_val is None or num <= max_val):
                return num
        print("Please enter a valid number" + (f" between {min_val} and {max_val}" if min_val is not None else "") + ".")

def choose_difficulty():
    print("\nChoose difficulty:")
    print("1) Easy   (1–50,  10 attempts)")
    print("2) Medium (1–100, 7 attempts)")
    print("3) Hard   (1–200, 6 attempts)")
    choice = get_int("Enter 1, 2, or 3: ", 1, 3)
    if choice == 1:
        return 1, 50, 10
    if choice == 2:
        return 1, 100, 7
    return 1, 200, 6

def play_round():
    low, high, attempts = choose_difficulty()
    secret = random.randint(low, high)
    print(f"\nI picked a number between {low} and {high}. You have {attempts} attempts!")

    for turn in range(1, attempts + 1):
        guess = get_int(f"[Attempt {turn}/{attempts}] Your guess: ", low, high)

        if guess == secret:
            print(f"🎉 Correct! {secret} was the number. You won in {turn} attempts.")
            return True, turn

        diff = abs(guess - secret)
        if guess < secret:
            hint = "Too low"
        else:
            hint = "Too high"

        # Extra warmth hint
        if diff <= max(2, (high - low) // 20):
            hint += " (very close!)"
        elif diff <= max(5, (high - low) // 10):
            hint += " (close)"

        print(hint)

    print(f"\nOut of attempts! The number was {secret}. Better luck next time.")
    return False, attempts

def play():
    print("=== Number Guessing Game ===")
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    play()


=== Number Guessing Game ===

Choose difficulty:
1) Easy   (1–50,  10 attempts)
2) Medium (1–100, 7 attempts)
3) Hard   (1–200, 6 attempts)
Enter 1, 2, or 3: 2

I picked a number between 1 and 100. You have 7 attempts!
[Attempt 1/7] Your guess: 60
Too high (close)
[Attempt 2/7] Your guess: 47
Too low
[Attempt 3/7] Your guess: 53
🎉 Correct! 53 was the number. You won in 3 attempts.

Play again? (y/n): n
Thanks for playing! 👋
