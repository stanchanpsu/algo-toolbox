function bubbleSort(list) {
    var n = list.length - 1;
    var notSorted;
    do {
        notSorted = false;
        for (var i = 0; i < n; i++) {
            if (list[i] > list[i+1]) {
                let temp = list[i];
                list[i] = list[i+1];
                list[i+1] = temp;
                notSorted = true;
            }
        }
    } while (notSorted)
    return list;
}

exports.bubbleSort = bubbleSort;