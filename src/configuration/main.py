# Imports packages
import os
import json

# Imports from /src folder
from functions.color import color

# Main function that configures the program
def configuration():
    
    with open("./src/messages/metadata.json", "r", encoding='utf-8') as f:
        data = json.load(f)

    os.system('cls' if os.name == 'nt' else 'clear')

    os.system('title ' + data["title"])

    for index, line in enumerate(data['logo'].split('\n')):
        orange = '255; 94; 0'
        yellow = '247; 255; 0'
        blue = '0; 150; 255'

        theme = yellow if index % 2 == 0 else orange

        message = color(text=line, fg=theme )
        message = message.replace("( o.o )", color(text="( o.o )", fg=blue, bold=True, fg_end_color= theme, reset= False ))
        
        print(message)

    print("\n\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n")

    print(f"{data['title']} \n{color(text=data['description'], fg='94; 94; 94')}")

    print("\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n")
