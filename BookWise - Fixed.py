#imports
import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

#import external files
import spell_casting_practice
import fantasy_character
import alchemy_puzzle


#tracks who is logged into the code
logged_in_user = None

#books data
books = [{
    "book_title": "Harry Potter and the Sorcerer's Stone",
    "genre": "Adventure,Fantasy",
    "publication_year": 1997,
    "target_audience": "9-12 year olds",
    "summary":
    "This book follows Harry Potter, a young boy who discovers that he’s actually a wizard wwhehen he receives his letter of acceptance to Hogwarts School of Witchcraft and Wizardry.",
    "cover_image": "harrypotterandthesorcerersstone.jpg"
}, {
    "book_title": "Percy Jackson and the Olympians: The Lightning Thief",
    "genre": "Adventure, Fantasy, Mythology",
    "publication_year": 2005,
    "target_audience": "9-14 year olds",
    "summary":
    "This book follows Percy Jackson, a young boy who discovers that he’s actually the son of a Greek god. With the help of his two friends, he must catch the thief who stole Zeus’s root bolt in order to prevent a civil war.",
    "cover_image": "thelightningthief.jpg",
}, {
    "book_title": "The Hunger Games",
    "genre": "Dystopian, Science Fiction",
    "publication_year": 2008,
    "target_audience": "Young adults",
    "summary":
    "The story is centered around 16-year old Katniss Everdeen who is participating in the Hunger Games, a televised fight to the death where 2 teenagers from each of the twelve Districts of Panem are chosen at random to compete in.",
    "cover_image": "thehungergames.jpg"
}, {
    "book_title": "To Kill a Mockingbird",
    "genre": "Southern Gothic, Bildungsroman",
    "publication_year": 1960,
    "target_audience": "Young adults, adults",
    "summary":
    "This is a classic novel set in southern Alabama during the Great Depression and explores themes of racial bias through the experiences of Scout and Jem, two young children.",
    "cover_image": "tokillamockingbird.jpg"
}, {
    "book_title": "The Hobbit",
    "genre": "Fantasy, Adventure",
    "publication_year": 1937,
    "target_audience": "All ages",
    "summary":
    "Bilbo Baggins, a hobbit, is whisked away on an unexpected journey by the wizard Gandalf and a group of dwarves to reclaim their homeland from the dragon Smaug.",
    "cover_image": "thehobbit.jpg"
}, {
    "book_title": "The Lord of the Rings: The Fellowship of the Ring",
    "genre": "Fantasy, Adventure",
    "publication_year": 1954,
    "target_audience": "Adults",
    "summary":
    "Frodo Baggins inherits a powerful ring from his uncle, which sets him on a perilous quest to destroy it before it falls into the hands of the dark lord Sauron.",
    "cover_image": "thefellowshipofthering.jpg"
}, {
    "book_title": "The Catcher in the Rye",
    "genre": "Fiction, Coming-of-age",
    "publication_year": 1951,
    "target_audience": "Young Adults, adults",
    "summary":
    "This book follows Holden Caulfield, a disenchanted teenager expelled from prep school, who wanders through New York City grappling with alienation, identity, and the phoniness of adult society.",
    "cover_image": "thecatcherintherye.jpg"
}, {
    "book_title": "The Alchemist",
    "genre": "Fiction, Philosophical ",
    "publication_year": 1988,
    "target_audience": "Young adults, adults",
    "summary":
    "This is a novel about Santiago, an Andalusian shepherd boy who embarks on a journey to fulfill his recurring dream of finding a treasure near the Egyptian pyramids. Along the way, he encounters mentors, falls in love, and most importantly, discovers the meaning of life.",
    "cover_image": "thealchemist.jpg"
}, {
    "book_title": "Pride and Prejudice",
    "genre": "Romance, Classic Literature",
    "publication_year": 1813,
    "target_audience": "Young adults, adults",
    "summary":
    "Jane Austen's rootpiece explores the societal norms and gender roles of early 19th-century England through thae tumultuous romance between Elizabeth Bennet and Mr. Darcy.",
    "cover_image": "prideandprejudice.jpg"
}, {
    "book_title": "The Great Gatsby",
    "genre": "Modernist, Tragedy",
    "publication_year": 1925,
    "target_audience": "Young adults, adults",
    "summary":
    "F. Scott Fitzgerald's novel paints a vivid portrait of the Roaring Twenties, delving into the lives of the enigmatic Jay Gatsby and his obsession with the elusive Daisy Buchanan, amidst themes of wealth, class, and the American Dream.",
    "cover_image": "thegreatgatsby.jpg"
}, {
    "book_title": "Animal Farm",
    "genre": "Political Satire, Allegory",
    "publication_year": 1945,
    "target_audience": "Adults",
    "summary":
    "George Orwell's allegorical novella explores the corruption of power and the dangers of totalitarianism, as a group of farm animals overthrow their human owner, only to succumb to their own internal power struggles and oppression.",
    "cover_image": "animalfarm.jpg"
}, {
    "book_title":
    "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe",
    "genre": "Fantasy, Children's Literature",
    "publication_year": 1950,
    "target_audience": "Children, Young adults",
    "summary":
    "C.S. Lewis's beloved fantasy follows the adventures of four siblings who discover the magical land of Narnia through a wardrobe, where they join the noble lion Aslan in his battle against the White Witch's tyranny.",
    "cover_image": "thelionthewitchandthewardrobe.jpg"
}, {
    "book_title": "Alice's Adventures in Wonderland",
    "genre": "Fantasy, Children's Literature",
    "publication_year": 1865,
    "target_audience": "Children, Young adults",
    "summary":
    "Lewis Carroll's whimsical tale follows young Alice as she falls down a rabbit hole into a fantastical world populated by peculiar creatures and nonsensical characters, challenging conventions and embracing imagination.",
    "cover_image": "alicesadventuresinwonderland.jpg"
}, {
    "book_title": "The Kite Runner",
    "genre": "Historical Fiction, Drama",
    "publication_year": 2003,
    "target_audience": "Adults",
    "summary":
    "Khaled Hosseini's novel follows Amir, a young boy from Afghanistan, as he grapples with guilt and redemption over betraying his childhood friend Hassan, against the backdrop of Afghanistan's tumultuous history.",
    "cover_image": "thekiterunner.jpg"
}, {
    "book_title": "Where the Crawdads Sing",
    "genre": "Mystery, Coming-of-age",
    "publication_year": 2018,
    "target_audience": "Adults",
    "summary":
    "Delia Owens's novel follows Kya Clark, a young girl living in the marshes of North Carolina, as she navigates abandonment, prejudice, and love. When a murder mystery rocks the small town, Kya finds herself at the center of suspicion, challenging her solitary existence.",
    "cover_image": "wherethecrawdadssing.jpg"
}, {
    "book_title": "A Brief History of Time",
    "genre": "Science, Popular Science",
    "publication_year": 1988,
    "target_audience": "Adults",
    "summary":
    "Stephen Hawking's groundbreaking book explores complex scientific concepts such as the nature of time, black holes, and the origins of the universe, making them accessible to a general audience and inspiring readers to ponder the mysteries of the cosmos.",
    "cover_image": "abriefhistoryoftime.jpg"
}, {
    "book_title": "The Secret History",
    "genre": "Mystery, Psychological Fiction",
    "publication_year": 1992,
    "target_audience": "Young adults, adults",
    "summary":
    "Donna Tartt's novel revolves around a group of classics students at an elite college who become entangled in a murder plot, delving into themes of morality, friendship, and the consequences of obsession.",
    "cover_image": "thesecrethistory.jpg"
}, {
    "book_title": "Charlotte's Web",
    "genre": "Children's Literature, Fantasy",
    "publication_year": 1952,
    "target_audience": "Children",
    "summary":
    "E.B. White's beloved tale follows the unlikely friendship between a pig named Wilbur and a spider named Charlotte, who saves Wilbur from slaughter by weaving messages in her web, showcasing themes of friendship, sacrifice, and the cycle of life.",
    "cover_image": "charlottesweb.jpg"
}, {
    "book_title": "Game of Thrones",
    "genre": "Fantasy,Drama",
    "publication_year": 1996,
    "target_audience": "Adults",
    "summary": "In the Seven Kingdoms of Westeros, noble families vie for control of the Iron Throne. Amidst political intrigue, betrayal, and supernatural threats, the Stark family of Winterfell finds itself drawn into a web of power struggles.",
    "cover_image": "gameofthrones.jpg"
}, {
    "book_title": "The Fault in Our Stars",
    "genre": "Young Adult, Contemporary Fiction",
    "publication_year": 2012,
    "target_audience": "Teenagers",
    "summary":
    "John Green's poignant novel revolves around Hazel Grace Lancaster, a sixteen-year-old cancer patient, who meets and falls in love with Augustus Waters, a fellow cancer survivor, at a support group. Their relationship is tested by illness and mortality, but it ultimately teaches them about love, loss, and the meaning of life.",
    "cover_image": "thefaultinourstars.jpg"
}]

#minigames dict for imported code
minigames = {
    "Harry Potter and the Sorcerer's Stone":spell_casting_practice,
    "Game of Thrones":fantasy_character,
    "The Alchemist":alchemy_puzzle
    
    }


# Functions

#below two functions just save a dictionary to a file for future use (ratings), and then load the dictionary from that file, done with json
def save_dict_to_file(dictionary, filename):
    """
    Save a dictionary to a file in JSON format.

    Parameters:
        dictionary (dict): The dictionary to be saved.
        filename (str): The name of the file to save the dictionary to.
    """
    with open(filename, 'w') as file:
        json.dump(dictionary, file)

def load_dict_from_file(filename):
    """
    Load a dictionary from a file in JSON format.

    Parameters:
        filename (str): The name of the file to load the dictionary from.

    Returns:
        dict: The "loaded" dictionary.
    """
    with open(filename, 'r') as file:
        dictionary = json.load(file)
    return dictionary

#create a dictionary within the ratings.txt file
ratings = load_dict_from_file("ratings.txt")
#retrieve that dictionary
reading_list = load_dict_from_file("reading_list.txt")

    
def login(logged_in_user):
    """
    Log in to the system.
    """
    #gets entries from the user input
    username = username_entry.get()
    password = password_entry.get()

    #can't login if your account was never registered
    with open("user_info.txt", "r") as file:
        users = file.readlines()
        if len(users) == 0:
            messagebox.showerror("Login Error", "No users registered yet. Please register.")
            return
        
        
        #if account is registered code proceeds
        for line in users:
            info = line.strip().split(":")
            if info[0] == username and info[1] == password:
                messagebox.showinfo("Login Successful", "Welcome back, " + username + "!")
                logged_in_user = username
                
                display_cover_images(username, password)
                return
    
    #if username or password is entered wrong, a warning shows up
    messagebox.showerror("Login Error", "Invalid username or password.")
    with open("user_info.txt", "r") as file:
        users = file.readlines()
        if username not in users:
            messagebox.showerror("Login Error", "Account does not exist. Please register")
            
    return logged_in_user


def register(logged_in_user):
    """
    Register a new user.
    """
    #gets entries from the user input
    username = username_entry.get()
    password = password_entry.get()
    #password must be greater than 5 characters
    while len(password) < 5:
        messagebox.showerror("Password Error", "Password must be at least 5 characters long.")
        return

    #'r' allows us to read through the previously existing file
    with open("user_info.txt", "r") as file:
        users = file.readlines()

        for line in users:
            if username in line:
                #if username exists, you must try again
                messagebox.showerror("Registration Error", "Username already exists. Please choose another.")
                return

    # Add the username and password to user_info file
    with open("user_info.txt", "a") as file:
        file.write(f"{username}:{password}\n")

    messagebox.showinfo("Registration Successful", "You have successfully registered!")
    #tracks who's currently logged in
    logged_in_user = username
    return logged_in_user
    
    #closes login/registration page
    display_cover_images(username, password)



def show_register():
    """
    Show the registration widgets.
    """
    #finally able to use it
    register_button.config(state="normal")
    login_button.config(state="disabled")
    # Remove register_link
    register_link.grid_remove()
    # Remove login_button
    login_button.grid_remove()  

def show_login():
    """
    Show the login widgets.
    """
    #unable to use this button unless the register_link button is clicked first
    register_button.config(state="disabled")
    login_button.config(state="normal")
    # Restore register_link
    register_link.grid()
    # Restore login_button
    login_button.grid()  


def save_ratings(ratings):
    """
    Save user ratings of books.

    Parameters:
        ratings (dict): The ratings dictionary to save.
    """
    #saves ratings to the file created above with json
    save_dict_to_file(ratings, "ratings.txt")


# Function to load the reading list from a file
def load_reading_list(reading_list, logged_in_user):
    """
    Load the reading list for the logged-in user.

    Returns:
        list: The reading list for the logged-in user.
    """
    user_reading_list = []

    if logged_in_user not in reading_list:
        reading_list[logged_in_user] = []
        save_dict_to_file(reading_list, "reading_list.txt")
    user_reading_list = reading_list[logged_in_user]
    
    return user_reading_list


def update_reading_list(reading_list, logged_in_user, user_reading_list):
    """
    Update the reading list for the logged-in user.

    Args:
        reading_list (dict): The reading list dictionary.
        logged_in_user (str): The username of the logged-in user.
        user_reading_list (list): The updated reading list for the logged-in user.
    """
    if logged_in_user not in reading_list:
        reading_list[logged_in_user] = []
    reading_list[logged_in_user] = user_reading_list
    save_dict_to_file(reading_list, "reading_list.txt")
    
    return reading_list
    
def open_book_info(book):
    """
    Pop-up window displaying information about a book.

    Parameters:
        book (dict): The book dictionary containing information about the book.
    """
    book_window = tk.Toplevel(root)
    book_window.title(book["book_title"])

    def add_to_reading_list(book_title):
        """
        Adds books not already part of the reading list to the reading list.
        """
         # Load the reading list
        user_reading_list = load_reading_list() 
        
        if book_title in user_reading_list:
            messagebox.showinfo("Reading List", f"{book_title} is already in your reading list!")
        else:
            user_reading_list.append(book_title)
            update_reading_list(user_reading_list)
            messagebox.showinfo("Reading List", f"{book_title} added to your reading list!")
    

    # Function to rate the book
    def rate_book(star):
        
        if logged_in_user not in ratings:
            ratings[logged_in_user] = dict()
        ratings[logged_in_user][book["book_title"]] = star
        #pass data to be saved
        save_ratings(ratings)
        update_rating(star)


    # Function to update the displayed rating
    def update_rating(star):
        """
        Update the displayed rating.

        Parameters:
            star (int): The number of stars selected.
        """

    
        for i in range(5):
            if i < star:
                star_buttons[i].config(image=yellow_star)
            else:
                star_buttons[i].config(image=blank_star)
        
    #display book_info
    info_header = f"{book['book_title']}\n"
    
    info_text = f"Genre: {book['genre']}\n"
    info_text += f"Publication Year: {book['publication_year']}\n"
    info_text += f"Target Audience: {book['target_audience']}\n"
    info_text += f"Short summary: {book['summary']}\n"
    info_header = tk.Label(book_window, text=info_header, justify="center", wraplength=400, padx=20, pady=20, font=("Helvetica",16))
    info_header.pack()

     # If the book has a minigame associated, add a button to play the game
    if book["book_title"] in minigames:
        game_module = minigames[book["book_title"]]
        play_game_button = tk.Button(book_window, text="Play a Game 🎮", command =game_module.run_game)
        play_game_button.pack(pady=10)
        
    info_label = tk.Label(book_window, text=info_text, justify="left", wraplength=400, padx=20, pady=20)
    info_label.pack()

     # Display the book cover image, resized
    cover_image = Image.open(book["cover_image"])
    cover_image = cover_image.resize((200, 300), Image.LANCZOS)
    cover_photo = ImageTk.PhotoImage(cover_image)
    cover_label = tk.Label(book_window, image=cover_photo)
    cover_label.image = cover_photo
    cover_label.pack()
    
    # Load star images for rating the books
    blank_star = Image.open("blank_star.png")
    blank_star = blank_star.resize((50, 50), Image.LANCZOS)
    blank_star = ImageTk.PhotoImage(blank_star)
    
    yellow_star = Image.open("yellow_star.png")
    yellow_star = yellow_star.resize((50, 50), Image.LANCZOS)
    yellow_star = ImageTk.PhotoImage(yellow_star)

    # Create star rating buttons
    rating_frame = tk.Frame(book_window)
    rating_frame.pack()

    # Check if book has a rating, if not set to 0
    if logged_in_user in ratings and book["book_title"] in ratings[logged_in_user]:
        initial_rating = ratings[logged_in_user][book["book_title"]]
    else:
        initial_rating = 0

    rating = tk.IntVar(value=initial_rating)
    rating.set(initial_rating)

    star_buttons = []
    for i in range(5):
        heart_button = tk.Label(rating_frame, image=blank_star)
        heart_button.bind("<Button-1>", lambda event, s=i + 1: rate_book(s))
        heart_button.pack(side="left", padx=2)
        star_buttons.append(heart_button)

    # Update displayed rating
    update_rating(initial_rating)

    #creating add_to_reading_list_button at the bottom of the popout page
    add_to_reading_list_button = tk.Button(book_window, text="Add to Reading List 📖", command=lambda: add_to_reading_list(book["book_title"]))  # Pass book_title
    add_to_reading_list_button.pack(pady=10)



def display_cover_images(username, password):
    """
    Display cover images of books in a grid layout.

    Parameters:
        username (str): The username.
        password (str): The password.
    """

    def on_enter(event):
        "The book buttons bg becomes light blue when the mouse hovers over it"
        event.widget.config(bg="lightblue")

    def on_leave(event):
        "The book buttons bg becomes white when the mouse stops hovering over it"
        event.widget.config(bg="white")
    
    # Store PhotoImage objects here
    cover_photos = []  
    window = tk.Toplevel(root)
    window.title("BookWise")
    window.geometry("1000x1000")
    
    title = tk.Label(window, text="BookWise Catalog", font=("Stencil", 25))
    title.pack()
    
    #addinng a scrollbar so users can see the entirety of the catalog
    main_frame = tk.Frame(window)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    frame_two = tk.Frame(my_canvas)
    my_canvas.create_window((0, 0), window=frame_two, anchor="nw")

    #display books in a 4 by 5 grid shape (done with pack as it cannot be used in combo with grid)
    columns = 4
    for i, book in enumerate(books):
        cover_image = Image.open(book["cover_image"])
        cover_image = cover_image.resize((200, 300), Image.LANCZOS)
        cover_photo = ImageTk.PhotoImage(cover_image)

        row = i // columns
        col = i % columns

        button = tk.Button(frame_two, image=cover_photo, command=lambda b=book: open_book_info(b))
        button.image = cover_photo
        button.grid(row=row, column=col, padx=20, pady=20)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    #menubar at the top of the screen (above the title)
    menubar = tk.Menu(window)
    menubar.add_command(label="My Account", command=lambda: view_account_info(username, password))
    menubar.add_command(label="Reading List", command=display_reading_list)

    #configure menu
    window.config(menu=menubar)
    root.withdraw()
    
    #create window icon in the to left corner of the screen
    image = Image.open("bookwise.png")
    photo = ImageTk.PhotoImage(image)
    window.iconphoto(False, photo)
    
    #initialize the book catalog window
    window.mainloop()


def view_account_info(username, password):
    """
    View account information.

    Parameters:
        username (str): The username.
        password (str): The password.
    """
    account_window = tk.Toplevel(root)
    account_window.title("My Account")
    account_window.geometry("400x200")  

    # Display current username
    username_label = tk.Label(account_window, text="Username: " + username)
    username_label.pack()

    
    def change_username():
        """
        Change the user's username for their login.
        """
        change_username_window = tk.Toplevel(root)
        change_username_window.title("Change Username")

        def submit_new_username():
            """Creation of the new username."""
            new_username = new_username_entry.get()
            # Check if the new username is not empty
            if new_username:
                # Update the username in the user_info file
                update_username_in_file(new_username)
                messagebox.showinfo("Username Changed", f"Your username has been changed to {new_username}.")
                change_username_window.destroy()  # Close the change username window after changing username
                # Update the displayed username on the "My Account" window
                username_label.config(text="Username: " + new_username)
            else:
                messagebox.showerror("Error", "New username cannot be empty.")

        def update_username_in_file(new_username):
            """Updates the new username in the user_info.txt file"""
            # Read the user_info file and update the username
            with open("user_info.txt", "r") as file:
                lines = file.readlines()
            with open("user_info.txt", "w") as file:
                for line in lines:
                    current_username, current_password = line.strip().split(":")
                    if current_username == username_entry.get():  # Match the current username
                        file.write(f"{new_username}:{current_password}\n")
                    else:
                        file.write(line)

        #labels and buttons displayed for account info window
        new_username_label = tk.Label(change_username_window, text="New Username:")
        new_username_label.pack()
        new_username_entry = tk.Entry(change_username_window)
        new_username_entry.pack()

        submit_button = tk.Button(change_username_window, text="Submit", command=submit_new_username)
        submit_button.pack()


    change_username_button = tk.Button(account_window, text="Change Username", command=change_username)
    change_username_button.pack()

    # Display current password, but no code to change it
    password_label = tk.Label(account_window, text="Password: " + password)
    password_label.pack()

    password_label_2 = tk.Label(account_window, text="Password cannot be changed")
    password_label_2.pack()


    
    def delete_account():
        """This function deletes the accounf of the user"""
        def confirm_delete():
            """Allows user to confirm their delete"""
            response = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete your account?")
            if response == 1:
                # Delete the username and password from the user_info file
                delete_from_file(username, password)
                messagebox.showinfo("Account Deleted", "Your account has been successfully deleted.")
                account_window.destroy()  # Close the account window after deletion

        def delete_from_file(username, password):
            """Updates the user_info.txt file by removing that username and password information"""
            # Read the user_info file and remove the line containing the username and password
            with open("user_info.txt", "r") as file:
                lines = file.readlines()
            with open("user_info.txt", "w") as file:
                for line in lines:
                    current_username, current_password = line.strip().split(":")
                    if current_username != username and current_password != password:
                        file.write(line)

        confirm_delete()


    # Button to delete account
    delete_account_button = tk.Button(account_window, text="Delete Account", command=delete_account, bg="red", fg="white")
    delete_account_button.pack(pady=20)



def display_reading_list():
    """
    Display the user's reading list.
    """
    reading_list = load_reading_list()  # Load the reading list from the file

    reading_list_window = tk.Toplevel(root)
    reading_list_window.title("Reading List")

    if len(reading_list) == 0:
        label = tk.Label(reading_list_window, text="Your reading list is empty.", padx=10, pady=5)
        label.pack()
    else:
        for i, book_title in enumerate(reading_list):
            for book in books:
                if book["book_title"] == book_title:
                    frame = tk.Frame(reading_list_window)
                    frame.pack(anchor="w")

                    # Display the book cover image
                    cover_image = Image.open(book["cover_image"])
                    cover_image = cover_image.resize((50, 70), Image.LANCZOS)
                    cover_photo = ImageTk.PhotoImage(cover_image)
                    cover_label = tk.Label(frame, image=cover_photo)
                    cover_label.image = cover_photo
                    cover_label.grid(row=i, column=0, padx=10, pady=5)

                    # Display the book title
                    title_label = tk.Label(frame, text=book_title, padx=10, pady=5)
                    title_label.grid(row=i, column=1, padx=10, pady=5)


def favorited_books():
    """
    Display user's favorited books.
    """

    # Load ratings from file
    with open("ratings.txt", "r") as file:
        for line in file:
            # Check if the line has the correct format (book_title:rating)
            parts = line.strip().split(":")
            if len(parts) == 2:

                book_title, rating = parts
                rating = int(rating)
                if rating >= 0 and rating <= 5:  # Check if rating is in valid range
                    ratings[book_title] = rating
                else:
                    print(f"Ignore invalid rating in line: {line.strip()}")


    # Filter out books with no ratings
    rated_books = {book_title: rating for book_title, rating in ratings.items()}

    # Sort books based on total number of stars
    sorted_books = sorted(books, key=lambda x: rated_books.get(x["book_title"], 0), reverse=True)

    # Display favorited books along with their total number of stars
    favorited_books_window = tk.Toplevel(root)
    favorited_books_window.title("Favorited Books")

    for i, book in enumerate(sorted_books):
        if book["book_title"] in rated_books:
            frame = tk.Frame(favorited_books_window)
            frame.pack(anchor="w")

            # Display the book cover image
            cover_image = Image.open(book["cover_image"])
            cover_image = cover_image.resize((50, 70), Image.LANCZOS)
            cover_photo = ImageTk.PhotoImage(cover_image)
            cover_label = tk.Label(frame, image=cover_photo)
            cover_label.image = cover_photo
            cover_label.grid(row=i, column=0, padx=10, pady=5)

            # Display the book title
            title_label = tk.Label(frame, text=book["book_title"], padx=10, pady=5)
            title_label.grid(row=i, column=1, padx=10, pady=5)

            # Display the total number of stars
            total_stars = rated_books.get(book["book_title"], 0)
            stars_label = tk.Label(frame, text=f"Total Stars: {total_stars}", padx=10, pady=5)
            stars_label.grid(row=i, column=2, padx=10, pady=5)
        else:
            print(f"Ignore book without rating: {book['book_title']}")


def enable_register_button():
    """
    Enable the register button that was previously disabled.
    """
    register_button.config(state="normal", cursor="hand2")

# --- Main ---
#initialize window
root = tk.Tk()
root.title("BookWise Login")
root.geometry("800x600")

#window icon in top left corner
image = Image.open("bookwise.png")
photo = ImageTk.PhotoImage(image)
root.iconphoto(False, photo)

#initialize the login structure: buttons, labels, entries, etc
login_frame = tk.Frame(root)
login_frame.pack(pady=50)

#title
login_title = Label(login_frame, text="BookWise Login", font=("Stencil", 25))
login_title.grid(row=0, column=0, columnspan=2, pady=10)

#entries for username and password
username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=1, column=0, padx=10)

username_entry = tk.Entry(login_frame)
username_entry.grid(row=1, column=1, padx=10)

password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=2, column=0, padx=10)

password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=2, column=1, padx=10)


#buttons for login, registration, and "Don't have an account?"
login_button = tk.Button(login_frame, text="Login", cursor="hand2", command=login)
login_button.grid(row=4, column=0, padx=10)

#originally disabled as I wanted to utilize the register_link button to replicate how creating an account on an actual website works
register_button = tk.Button(login_frame, text="Register", command=lambda: register(username_entry.get()), state="disabled")
register_button.grid(row=4, column=1, padx=10)

register_link = tk.Button(root, text="Don't have an account? Register here.", cursor="hand2", command=show_register)
register_link.pack()


root.mainloop()