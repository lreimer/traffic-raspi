const five = require("johnny-five");
const Raspi = require("raspi-io");

const board = new five.Board({
    io: new Raspi()
});

// LEDS = PIN (5,12,16,6,13,17)

board.on("ready", function() {
    const leds = [
        new five.Led('GPIO5'), new five.Led('GPIO12'), new five.Led('GPIO16'),
	new five.Led('GPIO6') ,new five.Led('GPIO13'), new five.Led('GPIO17')
    ]

    leds.forEach(led => {
        led.blink();
    });

    // When this script is stopped, turn the LED off
    // This is just for convenience
    this.on('exit', function() {
        leds.forEach(led => {
            led.stop().off();
        });
    });
});
