# New derived class for ws2812b.py
Original by https://github.com/benevpi/pico_python_ws2812b

# pico_ws2812b
a library for using WS2812b leds (aka neopixels) with Raspberry Pi Pico

![neopixels in action](
https://github.com/benevpi/pico_python_ws2812b/blob/main/pico_ws2812b.jpg)


You'll first need to save the three files ws2812b.py, my_ws2812b.py and optional my_rgb_colors.py to your device (for example, open it in Thonny and go file > save as and select MicroPython device. Give it the same name). Once it's there, you can import it into your code. 

You create an object with the parameters number of LEDs, state machine ID and GPIO number in that order. so, to create a strip of 10 leds on state machine 0 and GPIO 0, you use:

import my_ws2812b
import my_rgb_colors
```
strip = my_ws2812b.my_ws2812b(10,0,0)
```

```
#Set Pixel Number 1 to 3 red, green, blue (sry 4 german colornames (wip!))
strip.set_pixel2(0,my_rgb_colors.my_rgb_colors.ROT)
strip.set_pixel2(1,my_rgb_colors.my_rgb_colors.GRUEN)
strip.set_pixel2(2,my_rgb_colors.my_rgb_colors.BLAU)
strip.show()

#Set Strip to red
strip.fill2(my_rgb_colors.my_rgb_colors.ROT)
strip.show()
```

