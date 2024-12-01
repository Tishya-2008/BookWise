import keyboard
import pyautogui
import time
import random
from datetime import datetime

pyautogui.FAILSAFE = False
def type_random_words():
    # Extended list of words to type
    words = [
        "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
        "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
        "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yam", "zucchini",
        "apricot", "blackberry", "cantaloupe", "dragonfruit", "eggplant", "fennel", "guava",
        "huckleberry", "jackfruit", "kumquat", "lime", "mulberry", "nectar", "olive", "peach",
        "pomegranate", "radish", "spinach", "tomato", "ugni", "vegetable", "walnut", "ximenia"
    ]
    
    while True:
        current_time = datetime.now().time() 
        #word = random.choice(words)
        #keyboard.write(word)
        #keyboard.press_and_release('enter')
        x, y = pyautogui.size() # Get the screen size

        pyautogui.moveTo(random.randint(0, x), random.randint(0, y)) # Move to a random position on the screen
        time.sleep(9)

if __name__ == "__main__":
    type_random_words()