// by Alexander Nikolskiy

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine(line) {
    if (line !== "\n") {
        const n = parseInt(line.toString().split(' ')[0], 10);
        const m = parseInt(line.toString().split(' ')[1], 10);

        console.log(getFibMod(n, m));
        process.exit();
    }
}


function getFibMod(n, m) {
    // write your code here
    if (n <= 1) return n;

    let first = 0;
    let second = 1;

    for (let i = 1; i < n; i++) {
        [first, second] = [second, (first + second)%m]
    }

    return second;
}

module.exports = getFibMod;
