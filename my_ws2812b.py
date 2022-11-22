import ws2812b

class my_ws2812b(ws2812b.ws2812b):
    def __init__(self, num_leds, state_machine, pin=0, delay=0.001, break_pin=None):
        super().__init__(num_leds, state_machine, pin, delay)
        if break_pin != None:
            self.break_pin = Pin(break_pin, Pin.IN)
        else:
            self.break_pin = None
        
    def stop(self):
        if self.break_pin != None:
            return self.break_pin.value()
        else:
            return False
    
    def set_pixel3(self, pixel_num, red, green, blue, p_brightness = None):
        if p_brightness == None:
            super().set_pixel(pixel_num, red, green, blue)
        else:
            # Adjust color values with brightnesslevel
            blue = round(blue * (p_brightness / 255))
            red = round(red * (p_brightness / 255))
            green = round(green * (p_brightness / 255))

            self.pixels[pixel_num] = blue | red << 8 | green << 16
    
    def set_pixel2(self, pixel_num, p_color, p_brightness = None):
        if p_brightness == None:
            self.set_pixel3(pixel_num, round(float(p_color[0])), round(float(p_color[1])), round(float(p_color[2])))
        else:
            if p_brightness < 0:
                p_brightness = 0
            self.set_pixel3(pixel_num, round(float(p_color[0])), round(float(p_color[1])), round(float(p_color[2])), p_brightness)
    
    def set_pixel_line2(self, pixel1, pixel2, p_color):
        for i in range(pixel1, pixel2+1):
            self.set_pixel2(i, p_color)
            
    def fill2(self,p_color):
        super().fill(p_color[0], p_color[1], p_color[2])

# # Create a gradient with two RGB colors between "pixel1" and "pixel2" (inclusive) Version 2.0
    def set_pixel_line_gradient2(self, pixel1, pixel2, p1_color, p2_color):
        super().set_pixel_line_gradient(pixel1, pixel2, p1_color[0], p1_color[2], p1_color[2], p2_color[0], p2_color[1], p2_color[2])
    
    def get_color_pixel(self, pixel_num):
        for ii,cc in enumerate(self.pixels):
            #print(ii, pixel_num)
            if pixel_num == ii:
                r = int(((cc >> 8) & 0xFF)) # 8-bit red 
                g = int(((cc >> 16) & 0xFF)) # 8-bit green 
                b = int((cc & 0xFF)) # 8-bit blue
        return (r, g, b)
        
    def set_pixel_brightness(self, pixel_num, p_brightness = None):
        if p_brightness == None:
            pass
        else:
            dimmer_array = array.array("I", [0 for _ in range(self.num_leds)])
            dimmer_array = self.pixels
            for ii,cc in enumerate(self.pixels):
                #print(ii, pixel_num)
                if pixel_num == ii:
                    r = int(((cc >> 8) & 0xFF) * (p_brightness/255)) # 8-bit red dimmed to brightness
                    g = int(((cc >> 16) & 0xFF) * (p_brightness/255)) # 8-bit green dimmed to brightness
                    b = int((cc & 0xFF) * (p_brightness/255)) # 8-bit blue dimmed to brightness
                    if r > 255:
                        r = 255
                    if g > 255:
                        g = 255
                    if b > 255:
                        b = 255
                    dimmer_array[ii] = (g<<16) + (r<<8) + b # 24-bit color dimmed to brightness
            self.sm.put(dimmer_array, 8) # update the state machine with new colors
            time.sleep_ms(10)
