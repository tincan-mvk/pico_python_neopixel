import time
import my_ws2812b
import my_rgb_colors
import random

class lcl_Pixel:
    def __init__(self, id, offset, display, color, strip):
        self.id = id
        self.offset = offset
        self.display = display
        self.color = color
        self.position = offset
        self.strip = strip
        self.max_pix_idx = self.strip.num_leds-1
    def set_color(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def set_display(self, display):
        self.display = display
    def get_display(self):
        return self.display
    def set_offset(self, offset):
        self.offset = offset
    def get_offset(self):
        return self.offset
    def set_position(self, position):
        self.position = position
    def get_position(self):
        return self.position
    
    def calc_position(self, loop_idx):
        pos, rel_pos = divmod((loop_idx+self.get_offset()),(self.max_pix_idx+1))
        if pos%2 == 0:
            relativ_position = rel_pos
        else:
            relativ_position = self.max_pix_idx - rel_pos
        self.set_position(relativ_position)
        
        return self.get_position()
    
    def show(self, loop_idx):
        if self.get_display() == True:
            self.strip.set_pixel2(self.calc_position(loop_idx),self.get_color())
    
# General Setup
numpix = 20  # Number of NeoPixels
# Pin where NeoPixels are connected
strip = my_ws2812b.my_ws2812b(numpix, 0,0)
strip.fill(0,0,0)
color_pattern = []
color_pattern = my_rgb_colors.my_rgb_colors.rgb

delay = 0.03

max_brightness = 120
strip.brightness(80)

Pixels = []
# Definition of LEDs (max. 19)
for i in range(len(color_pattern)):
    Pixels.append(lcl_Pixel(i, i*7, True, color_pattern[i], strip))

turn = 0
while turn < 50:  
    turn += 1

    for i in range ((numpix)*2): #UP & DOWN       
        for pix in Pixels:
            pix.show(i)
        strip.show()
        #strip.fill(0,0,0)
        time.sleep(delay)

strip.fill(0,0,0)
strip.show()