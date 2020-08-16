import multiprocessing as mp
import NeoPixels
import numpy as np
import time

class Lantern_Manager():
    def __init__(self):
        self.lanterns = NeoPixels.create_lanterns()
        self.max_colors = ["FF0000", "00FF00", "0000FF", "FFFF00", "FF00FF", "00FFFF"]
        self.current_process = None

    def handle_current_process(self, lantern_id, pattern, hex_color, frequency):
        print(self.current_process)
        if self.current_process == None:
            self.current_process = mp.Process(target=self.change_pattern, args=(lantern_id, pattern, hex_color, frequency,))
            self.current_process.start()
        else:
            self.current_process.terminate()
            self.current_process.join()
            self.current_process = None
            self.handle_current_process(lantern_id, pattern, hex_color, frequency)

    def change_pattern(self, lantern_id, pattern, hex_color, frequency):
        r, g, b = self.hex_to_rgb(hex_color) if hex_color != None else (0, 0, 0)
        print(r, g, b)
        if pattern == "solid":
            self.lanterns[int(lantern_id)].solid_pattern(r, g, b)
        elif pattern == "random":
            while self.current_process != None:
                self.random_blink()

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.replace("#", "")
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        return r, g, b

    def clear_lantern_by_id(self, lantern_id):
        self.lanterns[lantern_id].clear_lantern()

    def random_blink(self, frequency=1.0):
        num_on = np.random.randint(1, 8)
        lanterns_on = [np.random.randint(0,8) for _ in range(num_on)]
        NeoPixels.clear_all_pixels()
        for n in lanterns_on:
            r, g, b = self.hex_to_rgb(self.max_colors[np.random.randint(0, len(self.max_colors))])
            self.lanterns[n].solid_pattern(r, g, b)
        time.sleep(1)

if __name__ == '__main__':
    lm = Lantern_Manager()
    lm.handle_current_process(3, 'solid', '000000', 1.0)