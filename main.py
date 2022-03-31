# Creates a letter using starting_letter.txt

with open('./Input/Letters/starting_letter.txt') as file:
    starting_letter = file.read()

with open('./Input/Names/invited_names.txt') as file:
    invited_names = file.read()

invited_names = invited_names.split()

name_index = starting_letter.find('[name]')
letters_to_send = []

for name in invited_names:
    letter = starting_letter[:name_index] + name + starting_letter[name_index + 6:]

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode='w') as file:
        file.write(letter)