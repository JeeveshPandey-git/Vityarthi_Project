import random

def start_game():
    #asks for input for number of players and player names
    print("===================================================")
    print("🎯 MULTI-PLAYER MULTI-ROUND NUMBER GUESSING GAME 🎯")
    print("===================================================")
    while True:
        try:
            N_Players = int(input("How many players are playing? "))
            if N_Players < 1:
                print("‼️ You need at least 1 player to play! Try again.‼️")
                continue
            break
        except ValueError:
            print("‼️ Invalid input! Please enter a whole number.‼️")

    players = []
    print("\n--- Player Registration ---")
    for i in range(1, N_Players+1):
        name = input(f"Enter name for Player {i}: ").strip()
        players.append(name if name else f"Player {i}")
    return players

def run_game_loop(players):
    #function for the management of the game rounds
    N_Players = len(players)
    scores = [0] * N_Players
    round_number = 1
    playing = True

    while playing:
        print(f"\n================ ROUND {round_number} ================")
        target_number = random.randint(1, 100)
        print("I have selected a secret number between 1 and 100.")
        print("Let the guessing begin!\n")

        round_over = False
        turn_index = 0

        while not round_over:
            current_index = turn_index % len(players)
            current_player = players[current_index]

            try:
                guess_str = input(f"▶️ {current_player}'s turn. Enter your guess: ")
                guess = int(guess_str)
            except ValueError:
                print("‼️ Invalid input! Please enter a whole number. You lose your turn!\n")
                turn_index += 1
                continue

            if guess < 1 or guess > 100:
                print("‼️ Out of bounds! Please guess between 1 and 100.\n‼️")
                turn_index += 1
                continue

            if guess == target_number:
                print( """
  ___________
 '._==_==_==_.'
 .-\\:      / -.

| (|:.     |) |
 '-\\:     | -'
   \\::.    /
    '::. .'
      ) (
    _.' '._
   `-------`
""")
                print(f"\n🥳 {current_player} WINS THE ROUND! 🥳")
                print(f"The secret number was indeed {target_number}!")

                scores[current_index] += 1
                round_over = True
            elif guess < target_number:
                print("⬊ Too low! The secret number is higher.⬆⬆⬆\n")
                turn_index += 1
            else:
                print("⬈ Too high! The secret number is lower.⬇⬇⬇\n")
                turn_index += 1

        print("\n🏆 CURRENT STANDINGS 🏆")
        for i in range(len(players)):
            print(f" - {players[i]}: {scores[i]} win(s)")

        while True:
            play_again = input("\nDo you want to play another round? (y/n): ").lower().strip()
            if play_again in ['y', 'yes']:
                round_number += 1
                break
            elif play_again in ['n', 'no']:
                playing = False
                break
            else:
                print("Please enter 'y' or 'n'.")
    return scores

def display_final_scoreboard(players, scores):
    #Displays the final scores and returns "\nThanks for playing!" so that it doesn't show none on the terminal after program is done running
    print("\n=========================================")
    print("🏁 FINAL SCOREBOARD 🏁")

    final_standings = sorted(zip(scores, players), reverse=True)

    for rank, (s, p) in enumerate(final_standings, 1):
        print(f" {rank}. {p} - {s} win(s)")
    return ("\nThanks for playing!")

def NumGame():
    players = start_game()
    scores = run_game_loop(players)
    return display_final_scoreboard(players, scores)

print(NumGame())
