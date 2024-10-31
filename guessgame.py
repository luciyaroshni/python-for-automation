#guess game

number = int(input("Guess your number"))
secret_number = 7

while secret_number != number:
    if secret_number > number:
        print("Your geuss is low")
    else:
        print("Your guess is high")
    number = int(input("Guess again"))

print("YOU GUESSED THE CURRECT NUMBER")
