def bubble_sort(items):
    '''Return array of items, sorted in ascending order'''

    length = len(items) - 1
    sorted = False
    while not sorted:
        sorted = True
        for element in range(0,length):
            if items[element] > items[element + 1]:
                hold = items[element + 1]
                items[element + 1] = items[element]
                items[element] = hold
                sorted = False
    return items

#####next

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''

    if len(items) < 2:
        return items

    result,mid = [],int(len(items)/2)

    y = merge_sort(items[:mid])
    z = merge_sort(items[mid:])

    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:result.append(z.pop(0))
            else:result.append(y.pop(0))

    result.extend(y+z)
    return result

#####next

def quick_sort(items):
    '''Return array of items, sorted in ascending order'''

    if len(items) <= 1:
        return items
    else:
        return quick_sort([x for x in items[1:] if x < items[0]]) + \
               [items[0]] + \
               quick_sort([x for x in items[1:] if x >= items[0]])
