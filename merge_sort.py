def merge_sort(list_to_sort):
    """ Sort the input list using the merge sort algorithm, and return it."""

    def merge(left, right):
        """ Return the merged left and right sorted (sub)lists."""
        if not left:
            return right
        if not right:
            return left
        if left[0] < right[0]:
            return [left[0]] + merge(left[1:], right)
        return [right[0]] + merge(left, right[1:])

    if len(list_to_sort) <= 1:
        return list_to_sort

    center = len(list_to_sort) // 2
    left = merge_sort(list_to_sort[:center])
    right = merge_sort(list_to_sort[center:])

    return merge(left, right)
