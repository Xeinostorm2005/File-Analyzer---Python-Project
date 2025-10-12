# Imports packages
import json

# Imports from /src folder
from functions.color import color

def main():
    data = {}

    with open('./src/messages/stage2.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
        data['title'] = content['title']
        data['message'] = content['message']
        data['not_found'] = content['not_found']
        data['empty'] = content['empty']

    print(color(text= data['title'], fg='255; 94; 0', bold= True ))
    
    message = data['message'].split(': ')

    print(": ".join([message[0], color(text= message[1], fg='94; 94; 94')]))


    while True:
        path = input(color(text='\n~> ', fg= '255; 94; 0'))

        if path.lower() == 'exit':
            exit()

        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    print(line)
        except FileNotFoundError:
            print(color(text= data['not_found'], fg='255; 0; 0'))
            continue

        break
    return 'completed'