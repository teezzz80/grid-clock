class GridDisplay:
    def __init__(self, col_list):
        self.col_list = col_list
        self.is_on = False


    def on(self):
        for col in self.col_list:
            col.on()
        self.is_on = True

    
    def off(self):
        for col in self.col_list:
            col.off()
        self.is_on = False


    def set_brightness(self, brightness):
        for col in self.col_list:
            col.set_brightness(brightness)


    def pattern(self, col, row, pattern_string, color=(0, 255, 0)):
        pattern_array = pattern_string.split()
        cursor_col = col
        cursor_row = row
        for pattern_row in pattern_array:
            for pattern_pixel in pattern_row:
                if pattern_pixel == "1":
                    pixel = self.col_list[cursor_col].pixel_list[cursor_row]
                    pixel.set_color(color)
                    pixel.on()
                cursor_col += 1
            cursor_col = col
            cursor_row += 1

    
    def message(self, message, color=(0, 255, 0)):
        self.off()
        self.pattern(0, 0, ALPHA_FONT[ALPHA_ENUM[message[0]]], color)
        self.pattern(4, 0, ALPHA_FONT[ALPHA_ENUM[message[1]]], color)
        self.pattern(0, 6, ALPHA_FONT[ALPHA_ENUM[message[2]]], color)
        self.pattern(4, 6, ALPHA_FONT[ALPHA_ENUM[message[3]]], color)
        

