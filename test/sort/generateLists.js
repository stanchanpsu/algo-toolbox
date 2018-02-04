var fs = require('fs');

const START = 0;
const END = 50;
const LENGTH = 20;
const LIST_FILE_NAME = 'ints.json'

function generateUnsortedInts(start, end, n) {
    var unsortedInts = [];
    for (var i = 0; i < n; i++) {
        var range = end - start;
        unsortedInts.push(Math.floor(Math.random()*range));
    }
    return unsortedInts;
}

function sortInts(ints) {
    function sortNum(a, b) {
        return a - b;
    } 
    return ints.concat().sort(sortNum);
}

module.exports = {
    generateUnsortedInts: generateUnsortedInts,
    sortInts: sortInts
}

var unsortedInts = generateUnsortedInts(START, END, LENGTH);
var sortedInts = sortInts(unsortedInts);
var listsObjectAsString = JSON.stringify({
    unsortedInts: unsortedInts,
    sortedInts: sortedInts
})

fs.writeFile('./test/sort/' + LIST_FILE_NAME, listsObjectAsString, (err) => {
    if (err) {
        console.log('Error writing file:', err);
    } else {
        console.log('File written: ', LIST_FILE_NAME);
    }
});