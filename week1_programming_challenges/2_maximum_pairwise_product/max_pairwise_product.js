// by Alexander Nikolskiy

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.once('line', () => {
    rl.on('line', readLine);
});

function readLine (line) {
    const arr = line.toString().split(' ').map(Number);

    console.log(max(arr));
    process.exit();
}


function max(arr) {
    let biggest = -Infinity;
    let second_biggest = -Infinity;
    for (const num of arr) {
        if (num > biggest) {
            second_biggest = biggest;
            biggest = num;
        } else if (num > second_biggest) {
            second_biggest = num;
        }
    }
    return biggest * second_biggest;
}


// function max_2(arr) {
//     // brute force solution with timeComplexity of O(n^2)
//     let max_product = 0;
//     let c_product;
//     for (let i = 0; i < arr.length; i++) {
//         for (let j = i+1; j < arr.length; j++) {
//              c_product = arr[i] * arr[j];
//              if (c_product > max_product) max_product = c_product;
//         }
//     }
//     return max_product;
// }


// function stresstests() {
//     while (true){
//         let arr = Array.from({length: 5}, () => Math.floor(Math.random() * 5));
//         let ans_1 = max(arr);
//         let ans_2 = max_2(arr);
//         if (ans_1 === ans_2) {
//             console.log(`Right ans \n${arr} \n${ans_1} || ${ans_2}`);
//         }else {
//             return `Wrong ans \n${arr} \n${ans_1} || ${ans_2}`
//         }
//     }
// }


module.exports = max;




