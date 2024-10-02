# Import necessary libraries
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pydirectinput

# Function to simulate a mouse click at given coordinates
def click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(random.uniform(0.001, 0.005))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(random.uniform(0.001, 0.005))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Function to simulate a double random throw click
def double_click_random_throw():
    click_random_throw()
    time.sleep(random.uniform(0.02, 0.025))
    click_random_throw()

# Function to simulate a random throw click
def click_random_throw():
    x, y = random.randint(960, 970), random.randint(520, 530)
    win32api.SetCursorPos((x, y))
    time.sleep(random.uniform(0.001, 0.005))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(random.uniform(0.001, 0.005))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Function to check for air bubbles on the screen
def check_air_bubbles_on_screen():
    s = pyautogui.screenshot()
    for x in range(770, 1160):
        for y in range(350, 730):
            colorcode = (68, 252, 234)  # Blue bubbles
            tempvar = False
            for x2 in range(5):
                if s.getpixel((x + x2, y)) == colorcode:
                    tempvar = True
                else:
                    tempvar = False
                    break
            if tempvar is True:
                return True
    return False

# Initialize counters and flags
counter = 0
fish_counter = 0
fish_found = False

# Main loop to check for fish and bubbles until 'q' is pressed
while keyboard.is_pressed('q') == False:
    if fish_counter < 3:
        # Check if fish is found
        if pyautogui.pixel(847, 820)[0] == 255 or pyautogui.pixel(860, 800)[0] == 255:
            # Reel in the fish
            click_random_throw()
            counter = 150  # Reset the counter
            fish_found = True

        # Increase fish counter if found
        if fish_found:
            if pyautogui.pixel(830, 800) != (83, 250, 83):
                fish_counter += 1
                print(f'Fish caught: {fish_counter}')
                fish_found = False
                time.sleep(1)

                # If fish counter reaches 3, stop all clicking and sell
                if fish_counter == 3:
                    print('Inventory full, selling...')
                    
                    # Pause all clicking and execute selling process
                    click(690, 962)
                    pyautogui.moveTo(1214, 959, duration=1)
                    click(1214, 959)
                    time.sleep(3)
                    click(1082, 343)
                    time.sleep(3)
                    click(1232, 420)
                    time.sleep(3)
                    click(1151, 421)
                    time.sleep(3)
                    click(1395, 360)
                    time.sleep(3)
                    
                    # Reset fish counter to 0 to resume fishing
                    fish_counter = 0
                    time.sleep(2)

        # If fish not found, check for air bubbles
        if not fish_found and check_air_bubbles_on_screen():
            # Reel in the fish
            click_random_throw()
            counter = 150
            fish_found = True

        if counter == 0:
            # Cast or reel in the fishing rod
            time.sleep(2)
            double_click_random_throw()
            counter = 150

        counter -= 1
        time.sleep(0.025)
    else:
        # When fish_counter is 3, clicking is paused and selling process will occur
        print("Pausing actions, inventory full...")
        time.sleep(1)  # Pausing while selling process happens
