from pyfiglet import Figlet
import sys,random

if not len(sys.argv) == 1 and not len(sys.argv) == 3:
    sys.exit("Invalid usage")
if not len(sys.argv) == 1:
     if not sys.argv[1] == "-f" and not sys.argv[1] == "--font":
         sys.exit("Invalid usage")


figlet = Figlet()
try:
    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")
except IndexError:
        figlet.setFont(font = random.choice(figlet.getFonts()))

text = input("Enter: ")
print(figlet.renderText(text))










