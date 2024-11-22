import time

text = input("Enter a text to animate: ")
animation_type = input("Choose animation type (1 for color swap, 2 for snake): ")
letters = text.upper()

# ANSI escape codes for colors
green = "\033[32m"
red = "\033[31m"
blue = "\033[34m"
reset = "\033[0m"

x = 0
while x < 5:
    if animation_type == "1":  # Color swap animation
        for i, letter in enumerate(letters):
            # Alternate between green, red, and blue
            if i % 3 == 0:
                color = green
            elif i % 3 == 1:
                color = red
            else:
                color = blue
            
            print(color + letter + reset, end=" ", flush=True)
            time.sleep(0.30)
        
        # Clear the screen
        print("\033[H\033[J", end="")
    
    elif animation_type == "2":  # Snake animation
        for i in range(len(letters)):
            # Print the current letter in green and the rest in reset color
            for j, letter in enumerate(letters):
                if j == i:
                    print(blue + letter + reset, end=" ", flush=True)
                else:
                    print(reset + letter, end=" ", flush=True)
            time.sleep(0.30)
            
            # Clear the screen
            print("\033[H\033[J", end="")
    
    x += 1
