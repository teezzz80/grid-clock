from constants import *

class GridDisplay:
    def __init__(self, np, col_list):
        self.np = np
        self.col_list = col_list
        self.brightness = 1
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

    
    def message(self, message, color=COLORS["green"]):
        self.off()
        msg = message.upper()
        self.pattern(0, 0, ALPHA_FONT[ALPHA_ENUM[msg[0]]], color)
        self.pattern(4, 0, ALPHA_FONT[ALPHA_ENUM[msg[1]]], color)
        self.pattern(0, 6, ALPHA_FONT[ALPHA_ENUM[msg[2]]], color)
        self.pattern(4, 6, ALPHA_FONT[ALPHA_ENUM[msg[3]]], color)
        

