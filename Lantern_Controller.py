import Neopixels

class Lantern_Manager():
    def __init__(self):
        self.lanterns = Neopixels.create_lanterns()

    def change_pattern(self, lantern_id, pattern, hex_color, frequency):
        int_lantern_id = lantern_id_to_int(lantern_id)
        r, g, b = self.hex_to_rgb(hex_color)
        if pattern == "solid":
            self.lanterns[int_lantern_id].solid_pattern(r, g, b)
    
    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.replace("#", "")
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        return r, g, b
        
    def lantern_id_to_int(self, lantern_id):
        return int(lantern_id)
