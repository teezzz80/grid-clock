class GridCol:
    def __init__(self, pixel_list):
        self.last_pattern = None
        self.is_on = False
        self.pixel_list = pixel_list

        
    def set_color(self, color):
        for pixel in self.pixel_list:
            pixel.set_color(color)
            
    
    def set_brightness(self, brightness):
        for pixel in self.pixel_list:
            pixel.set_brightness(brightness)
        

    def on(self):
        for pixel in self.pixel_list:
            pixel.on()
        self.is_on = True
            
    
    def off(self):
        for pixel in self.pixel_list:
            pixel.off()
        self.is_on = False
