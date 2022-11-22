import array, time, random        

class my_rgb_colors(object):

    rgb_dict = {
        "SCHWARZ": (0,0,0),
        "WEISS": (255,255,255),
        "ROT": (255,0,0),
        "LIMETTE": (0,255,0),
        "BLAU": (0,0,255),
        "GELB": (255,255,0),
        "CYAN": (0,255,255),
        "MAGENTA": (255,0,255),
        "SILBER": (192, 192, 192),
        "GRAU": (128, 128, 128),
        "KASTANIENBRAUN": (128,0,0),
        "OLIVE": (128,128,0),
        "GRUEN": (0,128,0),
        "LILA": (128,0,128),
        "BLAUGRUEN": (0,128,128),
        "MARINE": (0,0,128),
        "DUNKELROT": (139,0,0),
        "BRAUN": (165, 42, 42),
        "SCHAMOTTESTEIN": (178, 34, 34),
        "PURPUR": (220, 20, 60),
        "TOMATE": (255,99,71),
        "KORALLE": (255, 127, 80),
        "INDISCHROT": (205,92,92),
        "LEICHTEKORALLE": (240, 128, 128),
        "DUNKLERLACHS": (233, 150, 122),
        "LACHS": (250, 128, 114),
        "LEICHTERLACHS": (255, 160, 122),
        "ORANGEROT": (255,69,0),
        "DUNKELORANGE": (255, 140, 0),
        "ORANGE": (255,165,0),
        "GOLD": (255,215,0),
        "DUNKELGOLDENERSTAB": (184, 134, 11),
        "GOLDENERSTAB": (218, 165, 32),
        "BLASSGOLDENERSTAB": (238,232,170),
        "DUNKLESKHAKI": (189, 183, 107),
        "KHAKI": (240, 230, 140),
        "GELBGRUEN": (154, 205, 50),
        "DUNKELOLIVGRUEN": (85, 107, 47),
        "OLIVGRUEN": (107, 142, 35),
        "RASENGRUEN": (124,252,0),
        "GRUENGELB": (173, 255, 47),
        "DUNKELGRUEN": (0,100,0),
        "WALDGRUEN": (34, 139, 34),
        "LINDGRUEN": (50, 205, 50),
        "HELLGRUEN": (144, 238, 144),
        "BLASSESGRUEN": (152, 251, 152),
        "DUNKLESSEEGRUEN": (143, 188, 143),
        "MITTLERESFRUEHLINGSGRUEN": (0,250,154),
        "FRUEHLINGSGRUEN": (0,255,127),
        "MEERESGRUEN": (46, 139, 87),
        "MEDIUMAQUAMARINE": (102, 205, 170),
        "MITTLERESSEEGRUEN": (60, 179, 113),
        "HELLMEERGRUEN": (32, 178, 170),
        "DUNKLESSCHIEFERGRAU": (47,79,79),
        "DUNKLESCYAN": (0,139,139),
        "AQUA": (0,255,255),
        "HELLESCYAN": (224,255,255),
        "DUNKLESTUERKIS": (0,206,209),
        "TUERKIS": (64, 224, 208),
        "MITTLERESTUERKIS": (72, 209, 204),
        "BLASSTUERKIS": (175, 238, 238),
        "AQUAMARINE": (127, 255, 212),
        "PUDERBLAU": (176, 224, 230),
        "KADETTENBLAU": (95, 158, 160),
        "STAHLBLAU": (70, 130, 180),
        "KORNBLUMENBLAU": (100, 149, 237),
        "TIEFESHIMMELBLAU": (0,191,255),
        "DODGERBLAU": (30, 144, 255),
        "HELLBLAU": (173, 216, 230),
        "HIMMELBLAU": (135, 206, 235),
        "HELLHIMMELBLAU": (135, 206, 250),
        "MITTERNACHTSBLAU": (25,25,112),
        "DUNKELBLAU": (0,0,139),
        "MITTELBLAU": (0,0,205),
        "KOENIGSBLAU": (65, 105, 225),
        "BLAUVIOLETT": (138, 43, 226),
        "INDIGO": (75,0,130),
        "DUNKLESSCHIEFERBLAU": (72, 61, 139),
        "SCHIEFERBLAU": (106,90,205),
        "MITTELSCHIEFERBLAU": (123, 104, 238),
        "MITTELVIOLETT": (147, 112, 219),
        "DUNKLESMAGENTA": (139,0,139),
        "DUNKELVIOLETT": (148,0,211),
        "DUNKLEORCHIDEE": (153,50,204),
        "MITTLEREORCHIDEE": (186,85,211),
        "DISTEL": (216, 191, 216),
        "PFLAUME": (221,160,221),
        "VIOLETT": (238, 130, 238),
        "MAGENTA": (255,0,255),
        "ORCHIDEE": (218,112,214),
        "MITTELVIOLETTROT": (199, 21, 133),
        "HELLVIOLETTROT": (219,112,147),
        "DUNKELROSA": (255, 20, 147),
        "PINK": (255, 105, 180),
        "HELLPINK": (255, 182, 193),
        "ROSA": (255, 192, 203),
        "ALTWEISS": (250, 235, 215),
        "BEIGE": (245, 245, 220),
        "BISKUIT": (255,228,196),
        "BLANCHIERTEMANDEL": (255,235,205),
        "WEIZEN": (245,222,179),
        "MAISSEIDE": (255,248,220),
        "ZITRONENCHIFFON": (255, 250, 205),
        "HELLGOLDENERSTABGELB": (250, 250, 210),
        "HELLGELB": (255, 255, 224),
        "SATTELBRAUN": (139,69,19),
        "SIENNA": (160,82,45),
        "SCHOKOLADE": (210, 105, 30),
        "PERU": (205, 133, 63),
        "SANDBRAUN": (244, 164, 96),
        "KRAEFTIGESHOLZ": (222, 184, 135),
        "TAN": (210, 180, 140),
        "ROSIGBRAUN": (188, 143, 143),
        "MOKASSIN": (255,228,181),
        "NAVAJOWEISS": (255,222,173),
        "PFIRSICHBLAETTERTEIG": (255,218,185),
        "NEBLIGEROSE": (255,228,225),
        "LAVENDELERROETEN": (255,240,245),
        "LEINEN": (250, 240, 230),
        "ALTESPITZE": (253, 245, 230),
        "PAPAYAPEITSCHE": (255,239,213),
        "MUSCHEL": (255, 245, 238),
        "MINZCREME": (245,255,250),
        "SCHIEFERGRAU": (112, 128, 144),
        "HELLSCHIEFERGRAU": (119, 136, 153),
        "HELLSTAHLBLAU": (176, 196, 222),
        "LAVENDEL": (230, 230, 250),
        "BLUMENWEISS": (255, 250, 240),
        "ALICEBLAU": (240, 248, 255),
        "GEISTWEISS": (248,248,255),
        "HONIGTAU": (240, 255, 240),
        "ELFENBEIN": (255, 255, 240),
        "AZURBLAU": (240, 255, 255),
        "SCHNEE": (255, 250, 250),
        "DUNKELGRAU": (105, 105, 105),
        "MILDGRAU": (169, 169, 169),
        "SILBERGRAU": (192, 192, 192),
        "HELLGRAU": (211,211,211),
        "GAINSBORO": (220, 220, 220),
        "WEISSERRAUCH": (245, 245, 245),
    }

    SCHWARZ = (0,0,0)
    WEISS = (255,255,255)
    ROT = (255,0,0)
    LIMETTE = (0,255,0)
    BLAU = (0,0,255)
    GELB = (255,255,0)
    CYAN = (0,255,255)
    MAGENTA = (255,0,255)
    SILBER = (192, 192, 192)
    GRAU = (128, 128, 128)
    KASTANIENBRAUN = (128,0,0)
    OLIVE = (128,128,0)
    GRUEN = (0,128,0)
    LILA = (128,0,128)
    BLAUGRUEN = (0,128,128)
    MARINE = (0,0,128)
    DUNKELROT = (139,0,0)
    BRAUN = (165, 42, 42)
    SCHAMOTTESTEIN = (178, 34, 34)
    PURPUR = (220, 20, 60)
    TOMATE = (255,99,71)
    KORALLE = (255, 127, 80)
    INDISCHROT = (205,92,92)
    LEICHTEKORALLE = (240, 128, 128)
    DUNKLERLACHS = (233, 150, 122)
    LACHS = (250, 128, 114)
    LEICHTERLACHS = (255, 160, 122)
    ORANGEROT = (255,69,0)
    DUNKELORANGE = (255, 140, 0)
    ORANGE = (255,165,0)
    GOLD = (255,215,0)
    DUNKELGOLDENERSTAB = (184, 134, 11)
    GOLDENERSTAB = (218, 165, 32)
    BLASSGOLDENERSTAB = (238,232,170)
    DUNKLESKHAKI = (189, 183, 107)
    KHAKI = (240, 230, 140)
    GELBGRUEN = (154, 205, 50)
    DUNKELOLIVGRUEN = (85, 107, 47)
    OLIVGRUEN = (107, 142, 35)
    RASENGRUEN = (124,252,0)
    GRUENGELB = (173, 255, 47)
    DUNKELGRUEN = (0,100,0)
    WALDGRUEN = (34, 139, 34)
    LINDGRUEN = (50, 205, 50)
    HELLGRUEN = (144, 238, 144)
    BLASSESGRUEN = (152, 251, 152)
    DUNKLESSEEGRUEN = (143, 188, 143)
    MITTLERESFRUEHLINGSGRUEN = (0,250,154)
    FRUEHLINGSGRUEN = (0,255,127)
    MEERESGRUEN = (46, 139, 87)
    MEDIUMAQUAMARINE = (102, 205, 170)
    MITTLERESSEEGRUEN = (60, 179, 113)
    HELLMEERGRUEN = (32, 178, 170)
    DUNKLESSCHIEFERGRAU = (47,79,79)
    DUNKLESCYAN = (0,139,139)
    AQUA = (0,255,255)
    HELLESCYAN = (224,255,255)
    DUNKLESTUERKIS = (0,206,209)
    TUERKIS = (64, 224, 208)
    MITTLERESTUERKIS = (72, 209, 204)
    BLASSTUERKIS = (175, 238, 238)
    AQUAMARINE = (127, 255, 212)
    PUDERBLAU = (176, 224, 230)
    KADETTENBLAU = (95, 158, 160)
    STAHLBLAU = (70, 130, 180)
    KORNBLUMENBLAU = (100, 149, 237)
    TIEFESHIMMELBLAU = (0,191,255)
    DODGERBLAU = (30, 144, 255)
    HELLBLAU = (173, 216, 230)
    HIMMELBLAU = (135, 206, 235)
    HELLHIMMELBLAU = (135, 206, 250)
    MITTERNACHTSBLAU = (25,25,112)
    DUNKELBLAU = (0,0,139)
    MITTELBLAU = (0,0,205)
    KOENIGSBLAU = (65, 105, 225)
    BLAUVIOLETT = (138, 43, 226)
    INDIGO = (75,0,130)
    DUNKLESSCHIEFERBLAU = (72, 61, 139)
    SCHIEFERBLAU = (106,90,205)
    MITTELSCHIEFERBLAU = (123, 104, 238)
    MITTELVIOLETT = (147, 112, 219)
    DUNKLESMAGENTA = (139,0,139)
    DUNKELVIOLETT = (148,0,211)
    DUNKLEORCHIDEE = (153,50,204)
    MITTLEREORCHIDEE = (186,85,211)
    DISTEL = (216, 191, 216)
    PFLAUME = (221,160,221)
    VIOLETT = (238, 130, 238)
    MAGENTA = (255,0,255)
    ORCHIDEE = (218,112,214)
    MITTELVIOLETTROT = (199, 21, 133)
    HELLVIOLETTROT = (219,112,147)
    DUNKELROSA = (255, 20, 147)
    PINK = (255, 105, 180)
    HELLPINK = (255, 182, 193)
    ROSA = (255, 192, 203)
    ALTWEISS = (250, 235, 215)
    BEIGE = (245, 245, 220)
    BISKUIT = (255,228,196)
    BLANCHIERTEMANDEL = (255,235,205)
    WEIZEN = (245,222,179)
    MAISSEIDE = (255,248,220)
    ZITRONENCHIFFON = (255, 250, 205)
    HELLGOLDENERSTABGELB = (250, 250, 210)
    HELLGELB = (255, 255, 224)
    SATTELBRAUN = (139,69,19)
    SIENNA = (160,82,45)
    SCHOKOLADE = (210, 105, 30)
    PERU = (205, 133, 63)
    SANDBRAUN = (244, 164, 96)
    KRAEFTIGESHOLZ = (222, 184, 135)
    TAN = (210, 180, 140)
    ROSIGBRAUN = (188, 143, 143)
    MOKASSIN = (255,228,181)
    NAVAJOWEISS = (255,222,173)
    PFIRSICHBLAETTERTEIG = (255,218,185)
    NEBLIGEROSE = (255,228,225)
    LAVENDELERROETEN = (255,240,245)
    LEINEN = (250, 240, 230)
    ALTESPITZE = (253, 245, 230)
    PAPAYAPEITSCHE = (255,239,213)
    MUSCHEL = (255, 245, 238)
    MINZCREME = (245,255,250)
    SCHIEFERGRAU = (112, 128, 144)
    HELLSCHIEFERGRAU = (119, 136, 153)
    HELLSTAHLBLAU = (176, 196, 222)
    LAVENDEL = (230, 230, 250)
    BLUMENWEISS = (255, 250, 240)
    ALICEBLAU = (240, 248, 255)
    GEISTWEISS = (248,248,255)
    HONIGTAU = (240, 255, 240)
    ELFENBEIN = (255, 255, 240)
    AZURBLAU = (240, 255, 255)
    SCHNEE = (255, 250, 250)
    DUNKELGRAU = (105, 105, 105)
    MILDGRAU = (169, 169, 169)
    SILBERGRAU = (192, 192, 192)
    HELLGRAU = (211,211,211)
    GAINSBORO = (220, 220, 220)
    WEISSERRAUCH = (245, 245, 245)
    
    rainbow = [(128,0,0),
            (130,40,40),
            (141,83,59),
            (153,102,117),
            (153,102,169),
            (128,0,128),
            (101,0,155),
            (72,0,225),
            (4,0,208),
            (0,68,220),
            (1,114,226),
            (1,159,232),
            (11,175,162),
            (23,179,77),
            (0,212,28),
            (0,255,0),
            (128,255,0),
            (200,255,0),
            (255,255,0),
            (255,219,0),
            (255,182,0),
            (255,146,0),
            (255,109,0),
            (255,73,0),
            (255,0,0),
            (255,0,128),
            (255,105,180),
            (255,0,255),
            (168,0,185),]
    rgb = [(255,0,0),
            (0,255,0),
            (0,0,255),]
    
    def __init__(self):
        self.data = []
        self.preset_color_list = []
        
    def get_random_color(self):
        if len(self.preset_color_list) == 0:
            color_dict = rgb_colors.rgb_dict
            color_pattern = list(color_dict)
            return color_dict[color_pattern[random.randint(1, len(color_pattern) - 1)]]
        else:
            return self.preset_color_list[random.randint(1, len(self.preset_color_list) - 1)]
    
    def get_list_of_random_colors(self, num_of_colors):
        color_list = []
        for i in range(num_of_colors):
            color_list.append(self.get_random_color())
        return color_list
    
    def set_color_list(self, colorlist):
        self.preset_color_list = colorlist
        
    def reset_color_list(self, colorlist):
        self.preset_color_list = []
    
    def get_list_of_similar_colors(self, color, distance):
        color_list = []
        r_1, g_1, b_1 = color
        r1 = int(r_1)
        g1 = int(g_1)
        b1 = int(b_1)
        r1_min = int( r1 - distance )
        r1_max = int( r1 + distance )
        g1_min = int( g1 - distance )
        g1_max = int( g1 + distance )
        b1_min = int( b1 - distance )
        b1_max = int( b1 + distance )
        color_dict = rgb_colors.rgb_dict
        color_dict_list = list(color_dict)
        for i in range(len(color_dict_list)):
            r_2, g_2, b_2 = color_dict[color_dict_list[i]]
            r2 = int(r_2)
            g2 = int(g_2)
            b2 = int(b_2)
            #print(r1_min,r2,r1_max,g1_min,g2,g1_max,b1_min,b2,b1_max)
            if (r1_min) < r2 and (r1_max) > r2:
                if (g1_min) < g2 and (g1_max) > g2:
                    if (b1_min) < b2 and (b1_max) > b2:
                        color_list.append(color_dict[color_dict_list[i]])
        return color_list
    
    def build_gradient_pattern_from_two(self, p_color1, p_color2, length_pattern_part):
        pattern = []
        
        if p_color1 == p_color2 or length_pattern_part == 0: return

        right_pixel = length_pattern_part - 1 #max
        left_pixel = 0                    #min
        
        for i in range(right_pixel - left_pixel + 1):
            if i == 0:
                fraction = 0.5 / (right_pixel - left_pixel)
            else:
                fraction = i / (right_pixel - left_pixel)
            red = round(float(p_color2[0] - p_color1[0]) * fraction + float(p_color1[0]))
            green = round(float(p_color2[1] - p_color1[1]) * fraction + float(p_color1[1]))
            blue = round(float(p_color2[2] - p_color1[2]) * fraction + float(p_color1[2]))
            color = [red, green, blue]
            pattern.append(color)
        return pattern
    
    def get_color_from_rgb(self, red = 0, green = 0, blue = 0):
        if red > 255:
            red = 255
        if green > 255:
            green = 255
        if blue > 255:
            blue = 255
        if red < 0:
            red = 0
        if green < 0:
            green = 0
        if blue < 0:
            blue = 0
           
        return red, green, blue
    
    def hex_to_rgb(hex_val): #'#4285f4'
        return tuple(int(hex_val.lstrip('#')[ii:ii+2],16) for ii in (0,2,4)
                     
    def colorHSV(self, hue, sat, val):
            """
            seen at https://github.com/blaz-r/pi_pico_neopixel/neopixel.py
            Converts HSV color to rgb tuple and returns it.
            The logic is almost the same as in Adafruit NeoPixel library:
            https://github.com/adafruit/Adafruit_NeoPixel so all the credits for that
            go directly to them (license: https://github.com/adafruit/Adafruit_NeoPixel/blob/master/COPYING)
            :param hue: Hue component. Should be on interval 0..65535
            :param sat: Saturation component. Should be on interval 0..255
            :param val: Value component. Should be on interval 0..255
            :return: (r, g, b) tuple
            """
            if hue >= 65536:
                hue %= 65536

            hue = (hue * 1530 + 32768) // 65536
            if hue < 510:
                b = 0
                if hue < 255:
                    r = 255
                    g = hue
                else:
                    r = 510 - hue
                    g = 255
            elif hue < 1020:
                r = 0
                if hue < 765:
                    g = 255
                    b = hue - 510
                else:
                    g = 1020 - hue
                    b = 255
            elif hue < 1530:
                g = 0
                if hue < 1275:
                    r = hue - 1020
                    b = 255
                else:
                    r = 255
                    b = 1530 - hue
            else:
                r = 255
                g = 0
                b = 0

            v1 = 1 + val
            s1 = 1 + sat
            s2 = 255 - sat

            r = ((((r * s1) >> 8) + s2) * v1) >> 8
            g = ((((g * s1) >> 8) + s2) * v1) >> 8
            b = ((((b * s1) >> 8) + s2) * v1) >> 8

            return r, g, b
