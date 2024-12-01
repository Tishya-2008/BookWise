"""
U8 Final Project - Spell Casting Minigame
ICS3U
Tishya Bhat
Program explanation: This is a program where users combine elements to create a desired product.
Game creation day: May 10th, 2024
Program submission and completion: March 31st, 2024
"""

#imports
import tkinter as tk
from tkinter import messagebox
import random

#stops imported code from running immediately
def run_game():
    # Define the alchemy rules; constants
    ALCHEMY_RULES = {
        ('fire', 'earth'): 'lava',
        ('fire', 'air'): 'smoke',
        ('fire', 'water'): 'steam',
        ('earth', 'air'): 'dust',
        ('earth', 'water'): 'mud',
        ('air', 'water'): 'rain'
    }

    # Define the possible target products
    POSSIBLE_TARGET_PRODUCTS = ['lava', 'smoke', 'steam', 'dust', 'mud', 'rain']

    #if buttons clicked and no element made, call this
    def reset_buttons(buttons):
        """
        Resets the appearance of buttons to a "default" state.
        
        Args:
            buttons (dict): A dictionary containing button objects.
            
        Returns:
            None
        """
        for button in buttons.values():
            button.config(relief=tk.RAISED)

    #holds down one button while the other is waiting to be clicked
    def combine_elements(selected_elements, target_product, buttons):
        """
        Combines selected elements and checks if they match the target product.
        
        Args:
            selected_elements (list): A list containing the names of the selected elements.
            target_product (str): The target product to be created.
            buttons (dict): A dictionary containing button objects.
            
        Returns:
            None
        """
        #if two buttons selected
        if len(selected_elements) == 2:
            product = ALCHEMY_RULES.get(tuple(selected_elements), None)
            #does the combination produce the wanted product?
            if product:
                if product == target_product:
                    messagebox.showinfo("Congratulations", "You've created the target product!")
                else:
                    messagebox.showinfo("Result", f"You've created {product}. Try again!")
            else:
                messagebox.showinfo("Oops", "Those elements don't combine. Try again!")
            selected_elements.clear()
            reset_buttons(buttons)
            # Close the window after one round
            window.destroy()  

    # Function to handle element selection
    def select_element(element, selected_elements, buttons, target_product):
        """
        Handles the selection of elements by the user and checks to see whether 2 have been selected consecutively.
        
        Args:
            element (str): The name of the selected element.
            selected_elements (list): A list containing the names of the selected elements.
            buttons (dict): A dictionary containing button objects.
            target_product (str): The target product to be created.
            
        Returns:
            None
        """
        button = buttons[element]

        # Highlight the button with a blue border
        button.config(relief=tk.SOLID, bd=2, highlightbackground="blue")
        
        selected_elements.append(element)
        #2 elements selected
        if len(selected_elements) == 2:
            combine_elements(selected_elements, target_product, buttons)


    # Initialize tkinter window
    window = tk.Tk()
    window.title("Alchemy Puzzle")
    window.geometry("500x100")  # Set window size

    # Label to display the target product
    target_product = random.choice(POSSIBLE_TARGET_PRODUCTS)
    target_label = tk.Label(window, text=f"Target product: {target_product}")
    target_label.pack()

    selected_elements = []
    buttons = {}

    # Frame for buttons
    button_frame = tk.Frame(window)
    button_frame.pack()

    # Create buttons for each element
    for element in ['fire', 'earth', 'air', 'water']:
        button = tk.Button(button_frame, text=element, command=lambda element=element: select_element(element, selected_elements, buttons, target_product))
        button.pack(side=tk.LEFT)  # Pack buttons side by side
        buttons[element] = button


    window.mainloop()