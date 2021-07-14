import time
from constants import *

class GridDisplay:
    def __init__(self, np, col_list):
        self.np = np
        self.col_list = col_list
        self.brightness = 1
        self.theme_id = 0
        self.is_on = False


    def on(self):
        self.np.write()

    
    def off(self):
        self.clear()
        self.np.write()


    def clear(self):
        n = self.np.n
        for i in range(n):
            self.np[i] = (0, 0, 0)


    def get_raw_color(self, color, brightness):
        raw_color = [0, 0, 0]
        for i in range(3):
            raw_color[i] = int(color[i] * brightness)
        return tuple(raw_color)


    def set_brightness(self, brightness):
        self.brightness = brightness

    
    def increase_brightness(self, amount = 0.1):
        self.brightness += amount
        self.brightness = round(self.brightness, 1) if self.brightness <= 1 else 1
        self.message("BR" + str(self.brightness * 10).split(".")[0])
        time.sleep(1)


    def decrease_brightness(self, amount = 0.1):
        self.brightness -= amount
        self.brightness = round(self.brightness, 1) if self.brightness > 0 else 0.1
        self.message("BR" + str(self.brightness * 10).split(".")[0])
        time.sleep(1)

    
    def get_theme(self):
        return THEMES[self.theme_id]


    def get_theme_color(self, index):
        return COLORS[self.get_theme()[index]]


    def set_theme(self, theme_id):
        self.theme_id = theme_id

    
    def next_theme(self):
        self.theme_id += 1
        if self.theme_id >= len(THEMES):
            self.theme_id = 0
        self.set_theme(self.theme_id)


    def pattern(self, col, row, pattern_string, color=COLORS["green"]):
        pattern_array = pattern_string.split()
        cursor_col = col
        cursor_row = row
        for pattern_row in pattern_array:
            for pattern_pixel in pattern_row:
                if pattern_pixel == "1":
                    np_id = self.col_list[cursor_col][cursor_row]
                    self.np[np_id] = self.get_raw_color(color, self.brightness)
                cursor_col += 1
            cursor_col = col
            cursor_row += 1

    
    def get_char_pattern(self, char):
        return NUMBER_FONT[int(char)] if char.isdigit() else ALPHA_FONT[ALPHA_ENUM[char]]


    def message(self, message, color=COLORS["green"]):
        self.clear()
        msg = message.upper()
        msg_len = len(msg)
        if msg_len > 0:
            self.pattern(0, 0, self.get_char_pattern(msg[0]), color)
        if msg_len > 1:
            self.pattern(4, 0, self.get_char_pattern(msg[1]), color)
        if msg_len > 2:
            self.pattern(0, 6, self.get_char_pattern(msg[2]), color)
        if msg_len > 3:
            self.pattern(4, 6, self.get_char_pattern(msg[3]), color)
        self.on()
        

