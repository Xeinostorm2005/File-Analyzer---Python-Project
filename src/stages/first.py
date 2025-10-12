# Import Packages
import os
import json

# Import from /src folder
from functions.color import color

def main():
    data = {
        'length': 0,
        'selected_path': ''
    }

    with open('./src/messages/stage1.json', 'r') as f:
        content = json.load(f)
        data['title'] = content['title']
        data['message'] = content['message']
        data['not_found'] = content['not_found']
        data['empty'] = content['empty']
        data['select'] = content['select']
        data['invalid_option'] = content['invalid_option']
    
    print(color( text=data['title'], fg='255; 94; 0', bold=True ))

    paths = os.listdir('./input/')

    if len(paths) == 0:
        print(color( text=data['not_found'], fg='255; 0; 0' ))
        return 'not_found'
    else:
        print(data['message'])

        for index, path in enumerate(paths):
            print(color( text=f'{index + 1: >3} - {path}', fg='80; 80; 80' ))
            data['length'] += 1
        
        print(color( text=f'{'0':>3} - Exit', fg='94; 94; 94' ))


        print(f'\n{data['select'].replace('{length}', f'{data["length"]}')}')

        while True:
            try:
                select_path = int(input(color( text='~> ', fg='255; 94; 0', bold=True )))
                
                if select_path > data['length'] or select_path < 0:
                    raise ValueError
                
                break
            except ValueError:
                print(color( text=data['invalid_option'], fg='255; 0; 0' ))
            
        if select_path == 0:
            exit()
        else:
            data['selected_path'] = paths[select_path - 1]

        return 'completed'
