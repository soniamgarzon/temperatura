basic.forever(function on_forever() {
    basic.showNumber(input.temperature())
    if (input.temperature() > 25) {
        basic.showNumber(input.temperature())
        basic.showIcon(IconNames.Happy)
        basic.pause(500)
    } else {
        basic.showNumber(input.temperature())
        basic.showIcon(IconNames.Sad)
        basic.pause(500)
    }
    
})
