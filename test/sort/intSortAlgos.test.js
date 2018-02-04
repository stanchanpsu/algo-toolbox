const SORT_PATH = '../../sort/'

var bubbleSort = require(SORT_PATH + 'bubble').bubbleSort;
var insertionSort = require(SORT_PATH + 'insertion').insertionSort;
var selectionSort = require(SORT_PATH + 'selection').selectionSort;
var mergeSort = require(SORT_PATH + 'merge').mergeSort;
var quickSort = require(SORT_PATH + 'quick').quickSort;

var ints = require('./ints.json');
const PASSED = 'PASSED';
const FAILED = 'FAILED';


function testSort(name, algorithm) {
    var sorted = algorithm(ints.unsortedInts).toString();
    var answer = ints.sortedInts.toString();

    if (sorted === answer) {
        console.log('\x1b[32m', name, PASSED);
    } else {
        console.log('\x1b[31m', name, FAILED);
    }
}

testSort('bubble', bubbleSort);
testSort('insertion', insertionSort);
testSort('selection', selectionSort);
testSort('merge', mergeSort);
testSort('quick', quickSort);

