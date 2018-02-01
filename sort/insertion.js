function insertionSort(list) {
    var n = list.length;
    for (var i = 1; i < n; i++) {
        var item = list[i];
        var j = i - 1;
        while (item < list[j] && j >= 0) {
            list[j + 1] = list[j];
            j--;
        }
        list[j + 1] = item;
    }
    return list;
}

exports.insertionSort = insertionSort;