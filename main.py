import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

word_list = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'blizzard', 'boggle','galvanize', 'gazebo', 'gnarly', 'gnostic', 
'gossip', 'haphazard','icebox', 'injury', 'ivory', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'kiwifruit', 
'microwave', 'mnemonic', 'mystify', 'naphtha', 'pizazz', 'psyche', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 
'stretch', 'stronghold', 'stymied', 'subway']


lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for i in range(word_length):
    display+="_"
print(display)

game_start = True

while game_start:
    guess = input("Enter the guessed letter: ").lower()
    if guess in display:
        print(f"you have already chosen {guess}")
    for i in range(word_length):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]
    print(display)

    if "_" not in display:
        game_start = False
        print("You Won!!")

    if guess not in chosen_word:
        lives -= 1
        print(f"You have just {lives} left")
        if lives == 0:
            game_start = False
            print("You Lose!")
            print(f"The chosen word was: {chosen_word}")
print(stages[lives])


