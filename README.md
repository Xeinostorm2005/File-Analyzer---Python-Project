# File Analyzer - Python Project (NOT COMPLETED)
A Python-based text analysis tool that processes large books or documents. The program supports exporting results to multiple file types (e.g Json, Excel and Image)


## Sources
- Found a useful script to change the colors of a text in the terminal
```
https://stackoverflow.com/questions/74589665/how-to-print-rgb-colour-to-the-terminal
```
```
\033[38;2;146;255;12mHello!\033[0m
^     ^ ^  ^   ^   ^   ^     ^   ^ 
|     | |  R   G   B   |     |   |
|     | |  |           |     |   \ Reset the colour to default
|     | |  |           |     | 
|     | |  |           |     \ Escape character
|     | |  |           |
|     | |  \ R;G;B     \ Text to print
|     | |
|     | \ Indicate the following sequence is RGB
|     |
|     \ Code to instruct the setting of an 8 or 24-bit foreground (text) colour
|
\ Escape character
```
- Used this website to convert colors to RGB Color codes
- https://www.rapidtables.com/web/color/RGB_Color.html

- Learned a new built-in function called Enumerate().
- https://docs.python.org/3.14/library/functions.html#enumerate
