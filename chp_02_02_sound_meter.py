def sound level():
    max level = 0
    for i in range (0, 10):
        sound_level = (ping. read_analog() - 511) /100
        if sound_ level > max level:
            max_Level = sound_level
        return max level

def bargraph (a) :
    display.clear ()
    for y in range (0, 5) :
        if a > y:
            for x in range (0, 5) :
                display.set_pixel (x, 4-y, 9)

while True:
    bargraph (sound_level ())
    sleep (10)
