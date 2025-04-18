import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |   💀 GAME OVER! 💀
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
=========
''', '''
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
      |  🎉 START GAME 🎉
      |
=========
''']


winning_art = '''
      
  🎆 🎆 🎆 🎆 🎆 🎆 🎆
  🎉 CONGRATULATIONS! 🎉
  🎆 🎆 🎆 🎆 🎆 🎆 🎆
        (\O/) 
          |    🏆 YOU WIN!
         / \  

     
'''
word_list = [
    "aardvark", "baboon", "camel", "dolphin", "elephant", "flamingo", "giraffe", "hippopotamus", "iguana", "jaguar",
    "kangaroo", "lemon", "mango", "nectarine", "octopus", "penguin", "quokka", "rhinoceros", "strawberry", "tangerine",
    "tortoise", "umbrella", "vulture", "walrus", "xerus", "yak", "zebra", "adventure", "balloon", "camping", "discovery",
    "explorer", "forest", "hiking", "island", "journey", "kayaking", "mountain", "ocean", "paradise", "rafting",
    "trekking", "waterfall", "zenith", "calculator", "journal", "keyboard", "notebook", "pencil", "scissors", "xylophone",
    "scientist", "teacher", "veterinarian", "castle", "garden", "harbor", "observatory", "temple", "volcano",
    "botany", "cosmology", "forensics", "nanotechnology", "quantum", "robotics", "software", "transistor", "upload",
    "violin", "yodel", "zeppelin", "rainbow", "thunder", "hurricane", "earthquake", "fairy", "ghost", "haunted",
    "illusion", "necromancer", "phantasm", "runes", "sorcery", "wizard", "unicorn", "voodoo", "cyber", "database",
    "firewall", "internet", "joystick", "microchip", "robot", "wireless", "android", "zeppelin", "archer", "battle",
    "catapult", "dagger", "empire", "fortress", "gladiator", "infantry", "knight", "longbow", "monarchy", "warrior"
]

computer_choice = random.choice(word_list)
word_length = len(computer_choice)
word_display = ["_"] * word_length
lives = 6
end_of_game = False

print("🎉 Welcome to Hangman! 🎉")
print(f"The word has {word_length} letters. Try to guess it!")

while not end_of_game:
    print(stages[lives]) 
    print(f"LIVES LEFT: {lives} ❤️")
    print(f"Current word: {' '.join(word_display)}")
    
    guess_letter = input("GUESS A LETTER 🎯: ").lower()

    if guess_letter in word_display:
        print(f"⚠️ You already guessed '{guess_letter}'. Try another letter! ⚠️")
        continue

    if guess_letter in computer_choice:
        for index in range(word_length):
            if computer_choice[index] == guess_letter:
                word_display[index] = guess_letter
        print("✅ Correct guess!")
    else:
        lives -= 1
        print(f"❌ Wrong guess! '{guess_letter}' is not in the word.")

    print("-----------------------")

    if "_" not in word_display:
        print("🎉 CONGRATULATIONS! YOU WIN! 🎉")
        print(winning_art)
        end_of_game = True

    if lives == 0:
        print(stages[lives])  
        print("💀 YOU LOSE! 💀")
        print(f"The word was: {computer_choice}")
        end_of_game = True
