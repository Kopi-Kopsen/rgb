def on_button_a():
    for Index in range(30):
        strip.set_pixel_white_led(Index, 0)
        strip.show()
        basic.pause(200)
        strip.set_pixel_white_led(Index, 0)
        strip.show()
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB_RGB)
strip.set_brightness(50)

def on_forever():
    pass
basic.forever(on_forever)
