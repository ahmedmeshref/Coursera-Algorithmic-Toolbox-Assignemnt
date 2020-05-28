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

var memo = new Object()
function fib(n) {
    // write your code here
    if (n <= 1) return n
    if (n in memo) return memo[n]
    else {
        f = fib(n - 1) + fib(n - 2);
    }
    memo[n] = f;
    return f;

}

module.exports = fib;
