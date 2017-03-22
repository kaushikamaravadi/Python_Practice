"""Merge Sort"""


elements = [1,20,14,158,3]
def mergesort(elements):
    if len((elements)) == 1:
        return elements

    m = len(elements) // 2
    left = mergesort(elements[:m])
    right = mergesort(elements[m:])

    #if not len(left) or not len(right):
     #   return left or right

    result = []
    i = j = 0
    while (len(result) < len(right) + len(left)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result

print(mergesort(elements))
