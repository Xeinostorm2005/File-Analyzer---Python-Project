# Import Packages
import json

# Import from /src folder
from functions.color import color

def main():
    data = {

    }

    with open('./src/messages/stage3.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
        data['title'] = content['title']
        data['message'] = content['message']
        data['options'] = content['options']
        data['invalid_option'] = content['invalid_option']

    print(color({ 'text': data['title'], 'fg': '255; 94; 0', 'bold': True }))
    print(data['message'])

    for option in data['options']:
        print(color({ 'text': f'{option['value']:>3} - {option["label"]}', 'fg': '80; 80; 80' }))
    
    while True:
        try:
            select_option = int(input(color({ 'text': '\n~> ', 'fg': '255; 94; 0' })))

            if select_option < 0 or select_option > len(data['options']):
                raise ValueError
            
            break
        except ValueError:
            print(color({ 'text': data['invalid_option'], 'fg': '255; 0; 0' }))
            continue
    
    match select_option:
        case 1:
            print("hehe")
        case 2:
            print("hehe")
        case 3:
            print("hehe")
        case 4:
            print("hehe")
        case 0:
            exit()