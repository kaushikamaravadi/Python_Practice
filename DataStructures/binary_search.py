"""Binary Search"""

def binarysearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarysearch(alist[:midpoint], item)
            else:
                return binarysearch(alist[midpoint + 1:], item)

alist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
binarysearch(alist, 13)
