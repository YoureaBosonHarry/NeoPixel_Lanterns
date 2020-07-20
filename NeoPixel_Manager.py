import Neopixels

def change_pattern(lantern_id, pattern, hex_color, frequency):
    r, g, b = hex_to_rgb(hex_color)
    if pattern == "solid":
        lanterns[i].solid_pattern(r, g, b)
    
def hex_to_rgb(hex_color):
    hex_color = hex_color.replace("#", "")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return r, g, b
    
if __name__ == '__main__':
    lanterns = Neopixels.create_lanterns()
    
