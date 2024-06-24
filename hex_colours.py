HEX_COLOURS = {
    "AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Aqua": "#00ffff", "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff", "Beige": "#f5f5dc", "Bisque": "#ffe4c4", "Black": "#000000",
    "BlanchedAlmond": "#ffebcd", "Blue": "#0000ff"
}

colour_name = input("Enter colour name: ").capitalize()
while colour_name != "":
    print(f"{colour_name} is {HEX_COLOURS.get(colour_name, 'Invalid colour name')}")
    colour_name = input("Enter colour name: ").capitalize()
