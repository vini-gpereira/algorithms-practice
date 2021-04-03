'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the countSwaps function below.
function countSwaps(array) {
    const arraySize = array.length;
    
    let numSwaps = 0
    let arrayIsSorted = true;

    for (let i = arraySize; i >= 1; i--) {
        for (let j = 0; j < i - 1; j++) {
            const current = array[j];
            const next = array[j + 1];

            if (current > next) {
                swap(array, j, j + 1);
                arrayIsSorted = false;
                numSwaps++;
            } 
        }

        if (arrayIsSorted) {
            break;
        }

        arrayIsSorted = true;
    }

    console.log(`Array is sorted in ${numSwaps} swaps.`);
    console.log(`First Element: ${array[0]}`);
    console.log(`Last Element: ${array[arraySize - 1]}`);
}

function swap(array, i, j) {
    const aux = array[i];
    array[i] = array[j];
    array[j] = aux;
}

function main() {
    const n = parseInt(readLine(), 10);

    const a = readLine().split(' ').map(aTemp => parseInt(aTemp, 10));

    countSwaps(a);
}
