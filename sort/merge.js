function mergeSort(list) {
    var n = list.length;

    if (n === 1) {
        return list;
    }

    var mid = Math.ceil(n / 2);
    var left = list.slice(0, mid);
    var right = list.slice(mid, n);

    left = mergeSort(left);
    right = mergeSort(right);
    return merge(left, right);
}

function merge(left, right) {
    var leftLen = left.length;
    var rightLen = right.length;
    var merged = [];
    var i = 0;
    var j = 0;
    while (i <= leftLen && j <= rightLen) {
        if (i === leftLen) {
            restOfRight = right.slice(j, rightLen);
            return merged.concat(restOfRight);
        } else if (j === rightLen) {
            restOfLeft = left.slice(i, leftLen);
            return merged.concat(restOfLeft);
        } else if (left[i] <= right[j]) {
            merged.push(left[i]);
            i++;
        } else {
            merged.push(right[j]);
            j++;
        }
    }
}

exports.mergeSort = mergeSort;
exports.merge = merge;