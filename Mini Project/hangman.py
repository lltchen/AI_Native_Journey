import random
import os
import json
from pathlib import Path

# List of words to choose from
words = ['python', 'programming', 'computer', 'algorithm', 'database', 'network', 
         'developer', 'software', 'keyboard', 'monitor', 'internet']

# Score configuration
SCORE_CONFIG = {
    'correct_letter': 10,  # Points for each correct letter
    'word_completion': 50,  # Bonus points for completing a word
    'life_multiplier': 2,  # Additional points per remaining life
}

def load_high_score():
    """Load the high score from a file."""
    score_file = Path('high_score.json')
    if score_file.exists():
        with open(score_file, 'r') as f:
            return json.load(f)['high_score']
    return 0

def save_high_score(score):
    """Save the high score to a file."""
    with open('high_score.json', 'w') as f:
        json.dump({'high_score': score}, f)

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_hangman(tries):
    """Display the hangman based on remaining tries."""
    stages = [  # Final state: head, torso, both arms, both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Head, torso, both arms, one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # Head, torso, both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # Head, torso, one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # Head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # Head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # Initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def play_hangman():
    """Main game function."""
    word = random.choice(words).lower()
    word_letters = set(word)  # Letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # Letters guessed by the user
    
    lives = 6  # Number of tries before game over
    score = 0  # Current game score
    high_score = load_high_score()  # Load the high score

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        clear_screen()
        print('\nHigh Score:', high_score)
        print('Current Score:', score)
        print('You have', lives, 'lives left.')
        print('Used letters:', ' '.join(sorted(used_letters)))

        # Display the word with guessed letters
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(display_hangman(lives))
        print('Current word:', ' '.join(word_list))

        # Get user input
        user_letter = input('\nGuess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                # Calculate score for correct guess
                letter_count = word.count(user_letter)
                points = SCORE_CONFIG['correct_letter'] * letter_count
                bonus = SCORE_CONFIG['life_multiplier'] * lives
                score += points + bonus
                print(f'\nCorrect! +{points} points (Letter) +{bonus} points (Life bonus)')
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Please try again.')
        else:
            print('\nThat is not a valid letter.')

    # Game ended
    clear_screen()
    if lives == 0:
        print(display_hangman(lives))
        print('Sorry, you died. The word was', word)
        print(f'Final Score: {score}')
    else:
        # Award bonus points for completing the word
        completion_bonus = SCORE_CONFIG['word_completion']
        score += completion_bonus
        print('Congratulations! You guessed the word', word, '!!')
        print(f'Word completion bonus: +{completion_bonus} points')
        print(f'Final Score: {score}')

    # Update high score if necessary
    if score > high_score:
        print(f'\nNEW HIGH SCORE! Previous: {high_score}, New: {score}')
        save_high_score(score)
    
    return score

def main():
    """Main function to start the game."""
    total_score = 0
    games_played = 0
    
    while True:
        game_score = play_hangman()
        games_played += 1
        total_score += game_score
        
        print(f"\nSession Statistics:")
        print(f"Games Played: {games_played}")
        print(f"Total Score: {total_score}")
        print(f"Average Score: {total_score / games_played:.2f}")
        
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print("\nThanks for playing Hangman!")
    print(f"Final Session Statistics:")
    print(f"Games Played: {games_played}")
    print(f"Total Score: {total_score}")
    print(f"Average Score: {total_score / games_played:.2f}")

if __name__ == "__main__":
    main() 