
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine(line) {
    console.log(money_change(parseInt(line, 10)));
    process.exit();
}


money_change = m => {
    let m1 = m % 10;
    let m2 = m1 % 5;
    return Math.floor(m / 10) + Math.floor( m1 / 5) +
        Math.floor(m2)
}