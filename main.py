def on_forever():
    basic.show_number(input.temperature())
    if input.temperature() >= 25 and input.temperature() <= 34:
        basic.show_number(input.temperature())
        basic.show_icon(IconNames.HAPPY)
        basic.pause(500)
    else:
        basic.show_number(input.temperature())
        basic.show_icon(IconNames.SAD)
        basic.pause(500)
basic.forever(on_forever)
