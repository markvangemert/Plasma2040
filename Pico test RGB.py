import plasma
from plasma import plasma_stick

NUM_LEDS = 50 

led_strip = plasma.WS2812(
    NUM_LEDS, 0, 0, plasma_stick.DAT, rgbw=False, color_order=plasma.COLOR_ORDER_RGB
)

led_strip.start()

led_strip.set_rgb(0, 255, 0, 0) # eerste LED rood
led_strip.set_rgb(1, 0, 255, 0) # tweede LED groen
led_strip.set_rgb(2, 0, 0, 255) # derde LED blauw

# als de LEDS niet rood - groen - blauw kleuren, pas dan COLOR_ORDER_RGB op regel 7 aan
# zijn bv. de kleuren groen - rood - blauw, wijzig dan RGB in GRB
# gebruik deze kleurvolgorde in al je code
