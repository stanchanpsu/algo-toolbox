function quickSort(list) {
    return sort(list, 0, list.length - 1);
}

function sort(list, left, right) {
    if (left >= right) {
        return;
    }
    var pivot = list[Math.floor(left + (right - left) / 2)];
    var split = partition(pivot, list, left, right);
    sort(list, left, split - 1);
    sort(list, split, right);
    return list;
}

function partition(pivot, list, left, right) {
    while (left <= right) {
        while (list[left] < pivot) {
            left++;
        }
        while (list[right] > pivot) {
            right--;
        }
        if (left <= right) {
            var temp = list[right];
            list[right] = list[left];
            list[left] = temp;
            left++;
            right--;
        }
    }
    return left;
}

module.exports = {
    quickSort: quickSort,
    sort: sort,
    partition: partition
};