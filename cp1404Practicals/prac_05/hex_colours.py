

HEX_COLOURS = {"aquamarine1": "#7fffd4", "beige": "#f5f5dc", "black": "#000000", "BlueViolet": "#8a2be2",
               "brown": "#a52a2a", "CadetBlue": "#5f9ea0", "coral": "#ff7f50", "cyan1": "#00ffff",
               "DarkGreen": "#006400", "DarkOrange": "#ff8c00"}

colour = input("Enter colour: ")
while colour != "":
    if colour in HEX_COLOURS:
        print("{} is {}".format(colour, HEX_COLOURS[colour]))
    else:
        print("Invalid input.")
    colour = input("Enter colour: ")
