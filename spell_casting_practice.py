#imports
import tkinter as tk
from tkinter import *
import random

#stops imported code from running immediately
def run_game():
    def display_spell(current_spell=None):
        """
        Displays a random spell to be typed.
        
        Args:
            current_spell (str): The previously displayed spell. Initialized to None.

        Returns:
            new_spell (str): A random spell to be typed.
        """
        #random spell everytime
        spells = ["Lumos", "Alohomora", "Expelliarmus", "Expecto Patronum", "Accio", "Wingardium Leviosa", "Avada Kedavra", "Stupefy", "Imperio", "Crucio", "Protego", "Incendio"]
        new_spell = random.choice(spells)
        while new_spell == current_spell:
            new_spell = random.choice(spells)
        return new_spell

    def game():
        """
        Handles the spell casting game mechanics.
        """

        def on_enter_pressed(event=None):
            """
            Processes the user's input when Enter key is pressed.
            
            Args:
                event: The event (Enter key press). Initialized as None.

            Returns:
                None
            """
            nonlocal score, current_spell

            user_input = entry.get().strip().title()
            
            if user_input.lower() == current_spell.lower():
                score += 10
                score_label.config(text=f"Score: {score}")
                
            elif user_input.lower() != current_spell.lower() and score > 0:
                score -= 10
                score_label.config(text=f"Score: {score}")
                
            if len(user_input) > 0:
                entry.delete(0, END)
                current_spell = display_spell(current_spell)
                current_spell_label.config(text=current_spell)

        #30 seconds timer
        def countdown():
            """
            Counts down the time remaining for the game.
            """
            nonlocal time_remaining

            if time_remaining > 0:
                time_remaining -= 1
                time_label.config(text=f"Time Remaining: {time_remaining}")
                time_label.after(1000, countdown)
                
            else:
                game_over()

        #displays final score after the 30 seconds is up
        def game_over():
            """
            Displays the final score and offers the option to replay the game.
            """
            nonlocal score
            score_label.config(text=f"Final Score: {score}")
            entry.config(state='disabled')
            messagebox.showinfo("Game Over", f"Your final score is {score}! Congratulations! 🎉", parent=window)
            replay = messagebox.askyesno("Replay?", "Would you like to play again?", parent=window)
            if replay:
                #no replay = destroy window
                window.destroy()
                #replay game
                game()
            else:
                window.quit()

    # Initialize game variables
        score = 0
        time_remaining = 30
        current_spell = display_spell()

        # Hide start screen widgets
        start_title_label.pack_forget()
        start_instructions_label.pack_forget()
        start_button.pack_forget()

        # Show game screen widgets
        current_spell_label.pack()
        entry.pack()
        time_label.pack()
        score_label.pack()
        entry.focus_set()

        # Set initial values
        current_spell_label.config(text=current_spell)
        score_label.config(text=f"Score: {score}")
        time_label.config(text=f"Time Remaining: {time_remaining}")

        # Start countdown only once
        countdown()
        
        # Bind Enter key to on_enter_pressed function
        entry.bind("<Return>", on_enter_pressed)
        

    # Create main menu GUI
    window = tk.Tk()
    window.title("Spell Casting Practice")
    window.geometry("500x300")  # Set window size
    window.configure(bg='light blue')  # Set background color

    frame = Frame(window, bg='light blue')  # Create a frame to center the content
    frame.pack(expand=True)  # Center the content

    #instructions
    start_title_label = tk.Label(frame, text="Welcome to Spell Casting Practice!", font=("Helvetica", 20), bg='light blue')
    start_title_label.pack(pady=15)

    start_instructions_label = tk.Label(frame, text="You will see spell incantations appear on the screen.\nType them correctly within the time limit to score points.", font=("Helvetica", 12), bg='light blue')
    start_instructions_label.pack(pady=10)

    start_button = tk.Button(frame, text="Start Game", command=game, bg='white')
    start_button.pack(pady=10)

    #Checks whether the mouse is hovering over the widget
    def on_enter(event):
        """
        Changes the background color when the mouse hovers over the widget.
        """
        event.widget.config(bg="pink")

    #Checks for when the mouse is no longer hovering over the widget
    def on_leave(event):
        """
        Restores the background color when the mouse is no longer hovering over the widget.
        """
        event.widget.config(bg="white")


    #event listener, when there is a mouse on the start button it will turn pink, and when it leaves it will go back to white
    start_button.bind("<Enter>", on_enter)
    start_button.bind("<Leave>", on_leave)
            
    # Create game screen widgets (initially hidden)
    current_spell_label = tk.Label(frame, font=("Helvetica", 14), bg='light blue')
    entry = tk.Entry(frame, font=("Helvetica", 14))
    time_label = tk.Label(frame, font=("Helvetica", 12), bg='light blue')
    score_label = tk.Label(frame, font=("Helvetica", 12), bg='light blue')

    window.mainloop()