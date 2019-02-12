const Gpio = require('onoff').Gpio;

// LEDS = (5,12,16,6,13,17)
const leds = [
    new Gpio(5, 'out'), 
    new Gpio(12, 'out'),
    new Gpio(16, 'out'),
    new Gpio(6, 'out'),
    new Gpio(13, 'out'),
    new Gpio(17, 'out')
];

process.on('SIGINT', () => {
    leds.forEach(led => {
        led.unexport(); 
    });
});

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function ants() {
    while (true) {
        var prev = 0;
        for (let i = 0; i < leds.length; i++) {
            leds[prev].writeSync(0);
            leds[i].writeSync(1);
            prev = i;
            await sleep(1000);
        } 
    }
}

ants();