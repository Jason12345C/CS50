from pyfiglet import Figlet
import sys
import random
# if user wants random font
if len(sys.argv) == 1:
    user_input = input("Input: ")
    figlet = Figlet()
    list_of_fonts = figlet.getFonts()
    font = random.choice(list_of_fonts)
    figlet.setFont(font=font)
    print(figlet.renderText(user_input))

elif len(sys.argv) == 3:
    if sys.argv[1] == "--font" or sys.argv[1] == "-f":
        figlet = Figlet()
        list_of_fonts = figlet.getFonts()
        if sys.argv[2] in list_of_fonts:
            font = list_of_fonts[list_of_fonts.index(sys.argv[2])]
            figlet.setFont(font=font)
            user_input = input("Input: ")
            print(figlet.renderText(user_input))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

