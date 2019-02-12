const five = require("johnny-five");
const Raspi = require("raspi-io");

const board = new five.Board({
    io: new Raspi()
});

// LEDS = PIN (5,12,16,6,13,17)
const leds = [new five.Led(5), new five.Led(12), new five.Led(16), new five.Led(6), new five.Led(13), new five.Led(17)]

board.on("ready", function() {
    leds[0].blink();
    leds[1].blink();
    leds[2].blink();
    leds[3].blink();
    leds[4].blink();
    leds[5].blink();

    // When this script is stopped, turn the LED off
    // This is just for convenience
    this.on('exit', function() {
        leds[0].stop().off();
        leds[1].stop().off();
        leds[2].stop().off();
        leds[3].stop().off();
        leds[4].stop().off();
        leds[5].stop().off();
    });
});
