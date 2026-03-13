import random
correct_number = random.randint(1, 100)
while True:
    player_guess = input("Guess the number (1-100): ")
    if not player_guess.isdigit():
        print("Invalid input. Try again...")
        continue
    player_guess = int(player_guess)
    if player_guess == correct_number:
        print("You guessed it!")
        break
    if player_guess > correct_number:
        print("Too High!")
        continue
    else:
        print("Too Low!")
