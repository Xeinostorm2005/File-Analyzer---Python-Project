

# A function that colors the provided text
def color(text: str, fg: str = None, bg: str = None, bold: bool = False, fg_end_color: str = None, bg_end_color: str = None, end_bold: bool = False, reset: bool = True) -> str:

    # Sets to store temporary values
    style = { 'type': '', 'rgb': '', 'bold': '0' }
    end_style = { 'type': '', 'rgb': '', 'bold': '0' }

    # Change the color for the provided text
    if fg:
        style['type'] = '38'
        style['rgb'] = ';'.join(fg.split('; '))
    
    if bg:
        style['type'] = '48'
        style['rgb'] = ';'.join(bg.split('; '))
    
    if bold:
        style['bold'] = '1'
    
    # Change the color for characters after the provided text
    if fg_end_color:
        end_style['type'] = '38'
        end_style['rgb'] = ';'.join(fg_end_color.split('; '))
    
    if bg_end_color:
        end_style['type'] = '48'
        end_style['rgb'] = ';'.join(bg_end_color.split('; '))
    
    if end_bold:
        end_style['bold'] = '1'
    
    # Sets the theme for the provided text
    theme = f'\033[{style["bold"]};{style["type"]};2;{style["rgb"]}m'

    # Checks if the theme should be reset or not
    end = '\033[0m' if reset else ''

    # Checks if the characters after the provided text should be colored differently
    if fg_end_color or bg_end_color or end_bold and reset == False:
        end = f'\033[{end_style["bold"]};{end_style["type"]};2;{end_style["rgb"]}m{end}'

    # Sets the text
    text = text

    return f'{theme}{text}{end}'