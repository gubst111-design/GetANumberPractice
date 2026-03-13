import random
correct_number_level_1 = random.randint(1, 100)
correct_number_level_2 = random.randint(1, 200)
correct_number_level_3 = random.randint(1, 300)
attempts = 0
level = 1
while level == 1:
    player_guess = input("Guess the number (1-100): ")
    if not player_guess.isdigit():
        print("Invalid input. Try again...")
        continue
    if attempts >= 10:
        print("You lose! Please restart the game!")
        break
    player_guess = int(player_guess)
    if player_guess == correct_number_level_1:
        print("You guessed it!")
        level += 1
        attempts = 0
        break
    if player_guess > correct_number_level_1:
        print("Too High!")
        continue
    else:
        print("Too Low!")
    attempts += 1

while level == 2:
    player_guess = input("Guess the number (1-200): ")
    if not player_guess.isdigit():
        print("Invalid input. Try again...")
        continue
    if attempts >= 10:
        print("You lose! Please restart the game!")
        break
    player_guess = int(player_guess)
    if player_guess == correct_number_level_2:
        print("You guessed it!")
        level += 1
        attempts = 0
        break
    if player_guess > correct_number_level_2:
        print("Too High!")
        continue
    else:
        print("Too Low!")
    attempts += 1

while level == 3:
    player_guess = input("Guess the number (1-300): ")
    if not player_guess.isdigit():
        print("Invalid input. Try again...")
        continue
    if attempts >= 10:
        print("You lose! Please restart the game!")
        break
    player_guess = int(player_guess)
    if player_guess == correct_number_level_3:
        print("You guessed it!")
        level += 1
        attempts = 0
        break
    if player_guess > correct_number_level_3:
        print("Too High!")
    else:
        print("Too Low!")
    attempts += 1