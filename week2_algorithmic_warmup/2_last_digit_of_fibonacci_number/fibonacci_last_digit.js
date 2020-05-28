// by Alexander Nikolskiy

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine(line) {
    console.log(fib(parseInt(line, 10)));
    process.exit();
}

function fib(n) {
    // write your code here
    if (n <= 1) return n
    let first = 0;
    let second = 1;
    let temp;
    for (let i = 1; i < n; i++){
        temp = (first + second) % 10;
        [first, second] = [second, temp];
    }
    return second;
}

module.exports = fib;
