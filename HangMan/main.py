import tkinter as tk
import random

# Function to check if a letter is in the word
def check_letter(letter):
    global word, hidden_word, guesses_left
    if letter in word:
        index = word.find(letter)
        while index != -1:
            hidden_word = hidden_word[:index] + letter + hidden_word[index+1:]
            index = word.find(letter, index+1)
    else:
        guesses_left -= 1
        update_hangman()

# Function to update the hangman image
def update_hangman():
    hangman_canvas.delete("all")
    if guesses_left == 9:
        pass  # No body parts yet
    elif guesses_left == 8:
        hangman_canvas.create_oval(150, 150, 250, 250, fill="brown")  # Head
    elif guesses_left == 7:
        hangman_canvas.create_line(200, 150, 200, 50, width=5)  # Body
    elif guesses_left == 6:
        hangman_canvas.create_line(200, 100, 150, 150, width=5)  # Left arm
    elif guesses_left == 5:
        hangman_canvas.create_line(200, 100, 250, 150, width=5)  # Right arm
    elif guesses_left == 4:
        hangman_canvas.create_line(200, 50, 150, 0, width=5)  # Left leg
    elif guesses_left == 3:
        hangman_canvas.create_line(200, 50, 250, 0, width=5)  # Right leg
    elif guesses_left == 2:
        hangman_canvas.create_line(150, 75, 250, 75, width=5)  # Base
    elif guesses_left == 1:
        hangman_canvas.create_line(200, 75, 200, 125, width=5)  # Rope
    else:
        game_over("You lose!")

# Function to handle game over
def game_over(message):
    guess_button.config(state="disabled")
    guessed_letters_label.config(text=message)

# Function to handle correct guesses
def win_game():
    game_over("You win!")

# Create the main window
window = tk.Tk()
window.title("Hangman")

# Create the game elements
word = random.choice(["python", "programming", "computer", "science", "technology"])
hidden_word = "-" * len(word)
guesses_left = 10

guessed_letters_label = tk.Label(window, text="Guessed letters:")
guessed_letters_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()

guess_button = tk.Button(window, text="Guess", command=lambda: check_letter(guess_entry.get().lower()))
guess_button.pack()

word_label = tk.Label(window, text=hidden_word)
word_label.pack()

hangman_canvas = tk.Canvas(window, width=300, height=300)
hangman_canvas.pack()

# Start the game loop
window.mainloop()