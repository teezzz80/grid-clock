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


    def render_font(self, col, row, font_string):
        font_array = font_string.split()
        cursor_col = col
        cursor_row = row
        for font_row in font_array:
            for font_pixel in font_row:
                if font_pixel == "1":
                    self.col_list[cursor_col].pixel_list[cursor_row].on()
                cursor_col += 1
            cursor_col = col
            cursor_row += 1