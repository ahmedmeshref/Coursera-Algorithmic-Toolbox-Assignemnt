// by Alexander Nikolskiy

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');

rl.once('line', line => {
    const [itemsCount, knapsackCapacity] = line.toString().split(' ').map(Number);
    const values = [];
    const weights = [];
    let count = 0;

    rl.on('line', line => {
        const [v, w] = readLine(line);
        values.push(v);
        weights.push(w);

        if (++count >= itemsCount) {
            console.log(max(itemsCount, knapsackCapacity, values, weights));
            process.exit();
        }
    });
});

function readLine(line) {
    const v = parseInt(line.toString().split(' ')[0], 10);
    const w = parseInt(line.toString().split(' ')[1], 10);

    return [v, w];
}

function max(count, capacity, values, weights) {
    // write your code here
    let items = [],
        tot_val = 0,
        reminder;
    for (let i = 0; i < count; i++) {
        items.push([values[i], weights[i]]);
    }
    // so items by the value_per_unit
    items.sort((a, b) => (b[0] / b[1]) - (a[0] / a[1]))
    for (const [v, w] of items) {
        reminder = capacity - w;
        if (reminder >= 0) {
            tot_val += v;
            capacity = reminder
        } else {
            tot_val += (v/w) * capacity;
            return tot_val;
        }
    }
    return tot_val;
}

module.exports = max;



