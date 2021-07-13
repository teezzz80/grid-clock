class GridPixel:
    def __init__(self, np, np_id):
        self.brightness = 1
        self.np = np
        self.pixel = [np_id, (255, 0, 0), 1] # [id, (r, g, b), brightness]
        self.orig_color = self.pixel[1]
        self.orig_brightness = self.pixel[2]
        self.is_on = False
        
    
    def set_color(self, color):
        self.pixel[1] = color


    def set_brightness(self, brightness):
        self.pixel[2] = brightness


    def get_raw_color(self, color, brightness):
        raw_color = [0, 0, 0]
        for i in range(3):
            raw_color[i] = int(color[i] * brightness)
        return tuple(raw_color)


    def on(self):
        if self.is_off or self.orig_color != self.pixel[1] or self.orig_brightness != self.pixel[2]:
            self.np[self.pixel[0]] = self.get_raw_color(self.pixel[1], self.pixel[2])
            self.np.write()
            self.orig_color = self.pixel[1]
            self.orig_brightness = self.pixel[2]
        
    
    def off(self):
        self.np[self.pixel[0]] = (0, 0, 0)
        self.np.write()
    
        