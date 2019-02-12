const Gpio = require('onoff').Gpio;
var temporal = require("temporal");

// LEDS = (5,12,16,6,13,17)
const leds = [new Gpio(5, 'out'), new Gpio(12, 'out'), new Gpio(16, 'out'), new Gpio(6, 'out'), new Gpio(13, 'out'), new Gpio(17, 'out')];

temporal.queue([
    {
        delay: 1000,
        task: function() {
            leds[0].writeSync(1);
        }
    },
    {
        delay: 1000,
        task: function() {
            leds[0].writeSync(0);
            leds[1].writeSync(1);
        }
    },
    {
        delay: 1000,
        task: function() {
            leds[1].writeSync(0);
            leds[2].writeSync(1);
        }
    },
    {
        delay: 1000,
        task: function() {
            leds[2].writeSync(0);
        }
    }
]);

process.on('SIGINT', () => {
    leds.forEach(led => {
        led.writeSync(0);
        led.unexport();
    });
});
