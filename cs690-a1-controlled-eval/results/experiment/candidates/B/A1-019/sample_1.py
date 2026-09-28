def stable_partition(items, pivot):
    less = []
    greater_or_equal = []
    for item in items:
        if item < pivot:
            less.append(item)
        else:
            greater_or_equal.append(item)
    return less + greater_or_equal
