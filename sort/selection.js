function selectionSort(list) {
    var n = list.length;
    var index = 0;
    var min;
    while (index < n) {
        min = list[index];
        for (var i = index; i < n; i++) {
            if (list[i] <= min) {
                min = list[i];
                list[i] = list[index];
                list[index] = min;
            }
        }
        index++;
    }
    return list;
}

exports.selectionSort = selectionSort;