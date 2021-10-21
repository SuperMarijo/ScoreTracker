import datetime
import random
import json

with open("data_list.json", "r") as data_file:
    data_list = json.loads(data_file.read())

ordered_list = sorted(data_list, key=lambda x: x["attempts"])[:3]


for data_dict in ordered_list:
    results = "Player {0} guessed correctly it was number {1} in {2} tries on {3}.The wrong guesses were {4} Can you do better?"\
        .format(data_dict.get("player_name"),
                data_dict.get("secret_number"),
                str(data_dict.get("attempts")),
                str(data_dict.get("date")),
                data_dict.get("wrong_guesses"))
    print(results)

secret = random.randint(1, 99)
attempts = 0
player = input("What's your name? ")
wrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 99): "))
    attempts += 1

    if guess == secret:
        data_list.append({"attempts": attempts, "player_name": player, "secret_number": secret, "date": str(datetime.datetime.now()), "wrong_guesses": wrong_guesses})

        with open("data_list.json", "w") as data_file:
            data_file.write(json.dumps(data_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append({"wrong_guesses": guess})
