class GridPixel:
    def __init__(self, np, np_id):
        self.brightness = 1
        self.np = np
        self.pixel = [np_id, (255, 0, 0), 1] # [id, (r, g, b), brightness]
        
    
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
        self.np[self.pixel[0]] = self.get_raw_color(self.pixel[1], self.pixel[2])
        self.np.write()
        
    
    def off(self):
        self.np[self.pixel[0]] = (0, 0, 0)
        self.np.write()
    
        