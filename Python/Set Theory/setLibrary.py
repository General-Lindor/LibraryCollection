import copy

def connectionSet(Set):
    result = []
    for i in range(0, len(Set) - 1):
        for j in range(1, len(Set)):
            result.append([Set[i], Set[j]])
    return result

#for Lists: Order does not matter!
def compareUnordered(left, right):
    if isinstance(left, list):
        if isinstance(right, list):
            workspace = copy.deepcopy(left)
            workspace.extend(copy.deepcopy(right))
            eleDict = {}
            for element in workspace:
                if isinstance(element, list):
                    countLeft = 0
                    countRight = 0
                    for innerElement in left:
                        if compareUnordered(element, innerElement):
                            countLeft += 1
                    for innerElement in right:
                        if compareUnordered(element, innerElement):
                            countRight += 1
                    if countLeft != countRight:
                        return False
                else:
                    if eleDict.get(element) != True:
                        if left.count(element) != right.count(element):
                            return False
                        else:
                            eleDict[element] = True
            return True
        else:
            return False
    else:
        if left == right:
            return True
        else:
            return False

#for Lists: Order does matter!
def compareOrdered(left, right):
    if isinstance(left, list):
        if isinstance(right, list):
            length = len(left)
            if length != len(right):
                return False
            for i in range(length):
                if not compareOrdered(left[i], right[i]):
                    return False
            return True
        else:
            return False
    else:
        if left == right:
            return True
        else:
            return False

def intersectionSetOrdered(A, B):
    result = []
    for a in A:
        for b in B:
            if compareOrdered(a, b):
                result.append(a)

def intersectionSetUnordered(A, B):
    result = []
    for a in A:
        for b in B:
            if compareUnordered(a, b):
                result.append(a)

#A ohne B, order does matter
def relativeComplementOrdered(A, B):
    newA = copy.deepcopy(A)
    i = 0
    while i < len(newA):
        j = 0
        while j < len(B):
            if compareOrdered(newA[i], B[j]):
                newA.pop(i)
                if i == len(newA):
                    break
                j = 0
            else:
                j += 1
        i += 1
    return newA

#A ohne B, order doesn't matter
def relativeComplementUnordered(A, B):
    newA = copy.deepcopy(A)
    i = 0
    while i < len(newA):
        j = 0
        while j < len(B):
            if compareUnordered(newA[i], B[j]):
                newA.pop(i)
                if i == len(newA):
                    break
                j = 0
            else:
                j += 1
        i += 1
    return newA