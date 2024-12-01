"""
U8 Final Project - Game of Thrones Character Minigame
ICS3U
Tishya Bhat
Program explanation: This is a program where users input their gender and initials in order to create their very own Game of Thrones universe character name.
Game creation day: May 16th, 2024
Program submission and completion: March 31st, 2024
"""

#imports
import tkinter as tk
from tkinter import messagebox

 # Constants
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#stops imported code from running immediately
def run_game():
    def generate_character_name(first_name_letter, last_name_letter, gender):
        """
        Generates a Game of Thrones character name based on user input.

        Args:
            first_name_letter (str): The first letter of the first name.
            last_name_letter (str): The first letter of the last name.
            gender (str): The gender of the character. Either 'm' for male or 'f' for female.

        Returns:
            str: The generated Game of Thrones character name.
        """
        # Define fantasy first names for male and female, and famous houses as last names
        male_first_names = {
            'a': 'Aldar',
            'b': 'Baelor',
            'c': 'Cassius',
            'd': 'Daelon',
            'e': 'Elric',
            'f': 'Fyrian',
            'g': 'Galdor',
            'h': 'Haven',
            'i': 'Ilaric',
            'j': 'Jorath',
            'k': 'Kyran',
            'l': 'Lysander',
            'm': 'Myron',
            'n': 'Neris',
            'o': 'Orin',
            'p': 'Pyran',
            'q': 'Quinlan',
            'r': 'Rydan',
            's': 'Sorin',
            't': 'Tyrion',
            'u': 'Uldric',
            'v': 'Vaelor',
            'w': 'Wyland',
            'x': 'Xyris',
            'y': 'Ysara',
            'z': 'Zephyr'
        }
        
        female_first_names = {
            'a': 'Aria',
            'b': 'Brynn',
            'c': 'Cassia',
            'd': 'Dahlia',
            'e': 'Elara',
            'f': 'Fira',
            'g': 'Galadriel',
            'h': 'Haven',
            'i': 'Ivy',
            'j': 'Jasmine',
            'k': 'Kyra',
            'l': 'Luna',
            'm': 'Myra',
            'n': 'Nova',
            'o': 'Olivia',
            'p': 'Piper',
            'q': 'Quinn',
            'r': 'Rhea',
            's': 'Sylvia',
            't': 'Talia',
            'u': 'Unity',
            'v': 'Violet',
            'w': 'Willow',
            'x': 'Xena',
            'y': 'Yara',
            'z': 'Zara'
        }

        last_names = {
            'a': 'Arryn',
            'b': 'Baratheon',
            'c': 'Clegane',
            'd': 'Dayne',
            'e': 'Estermont',
            'f': 'Frey',
            'g': 'Greyjoy',
            'h': 'Hightower',
            'i': 'Ironwood',
            'j': 'Jordayne',
            'k': 'Karstark',
            'l': 'Lannister',
            'm': 'Martell',
            'n': 'Nymeros',
            'o': 'Osgrey',
            'p': 'Piper',
            'q': 'Qorgyle',
            'r': 'Redwyne',
            's': 'Stark',
            't': 'Tarly',
            'u': 'Umber',
            'v': 'Vance',
            'w': 'Westerling',
            'x': 'Xhobar',
            'y': 'Yronwood',
            'z': 'Zapalac'
        }

        # Get the corresponding first name based on gender
        if gender.lower().strip() == 'm':
            first_name = male_first_names.get(first_name_letter.lower())
        elif gender.lower().strip() == 'f':
            first_name = female_first_names.get(first_name_letter.lower())


        # Get the corresponding last name
        last_name = last_names.get(last_name_letter.lower())

        # Create the Game of Thrones character name
        character_name = f"{first_name} {last_name}"

        return character_name

    def generate_character():
        """
        Generates a Game of Thrones character name based on user input.
        Displays the generated character name and clears the input fields.
        
        Args:
            None
            
        Returns:
            None
        """
        gender = gender_var.get()
        first_name_letter = first_name_entry.get().strip().lower()
        last_name_letter = last_name_entry.get().strip().lower()

        if first_name_letter not in ALPHABET or last_name_letter not in ALPHABET:
            # Show error message if initials are not valid letters
            messagebox.showerror("Error", "Please enter valid letters for initials.")
            return

        # Generate the character name
        character_name = generate_character_name(first_name_letter, last_name_letter, gender)
        result_label.config(text=f"Your Game of Thrones character name is: {character_name}")

        # Clear the initial entries
        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)

    # Initialize tkinter window
    window = tk.Tk()
    window.geometry("500x300")  # Set window size

    window.title("Game of Thrones Character Name Generator")


    # Title
    title_label = tk.Label(window, text="What's your Game of Thrones name?\n", font=("Helvetica", 20))
    title_label.grid(row=0, column=0, columnspan=3, padx=5, pady=10)

    # Gender Input
    gender_label = tk.Label(window, text="Select your gender:")
    gender_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    gender_var = tk.StringVar(value='m')
    male_button = tk.Radiobutton(window, text='Male', variable=gender_var, value='m')
    male_button.grid(row=1, column=1, padx=5, pady=5)
    female_button = tk.Radiobutton(window, text='Female', variable=gender_var, value='f')
    female_button.grid(row=1, column=2, padx=5, pady=5)

    # First Name Initial Input
    first_name_label = tk.Label(window, text="Enter the first letter of your first name:")
    first_name_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    first_name_entry = tk.Entry(window)
    first_name_entry.grid(row=2, column=1, padx=5, pady=5)

    # Last Name Initial Input
    last_name_label = tk.Label(window, text="Enter the first letter of your last name:")
    last_name_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    last_name_entry = tk.Entry(window)
    last_name_entry.grid(row=3, column=1, padx=5, pady=5)

    # Generate Button
    generate_button = tk.Button(window, text="Generate", command=generate_character)
    generate_button.grid(row=4, column=0, columnspan=3, padx=5, pady=10)

    # Result Label
    result_label = tk.Label(window, text="")
    result_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

    window.mainloop()