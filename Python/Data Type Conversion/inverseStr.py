import copy
#inversion of str() operation for each element / key/ value of a complex datastructure; automatically checks if it's possible
def convert(t):
    
    def convertSingle(s):
        check = False
        if s == "True":
            s = True
            check = True
        elif s == "False":
            s = False
            check = True
        else:
            nums = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
            if isinstance(s, str):
                check = True
                for c in s:
                    if (not (c in nums)):
                        check = False
                        break
                if check:
                    s = int(s)
        return s, check
    
    if isinstance(t, dict):
        newT = {}
        for key, value in t.items():
            newKey, checkKey = convertSingle(key)
            newValue, checkValue = convertSingle(value)
            if checkKey:
                if checkValue:
                    if t.get(newKey) == None:
                        newT[newKey] = newValue
                    else:
                        newT[key] = newValue
                else:
                    if t.get(newKey) == None:
                        newT[newKey] = value
                    else:
                        newT[key] = value
            elif checkValue:
                newT[key] = newValue
            else:
                newT[key] = value
        t = newT
                
    elif isinstance(t, list):
        i = 0
        while i < len(t):
            t[i], check = convertSingle(t[i])
            i += 1
                
    elif isinstance(t, tuple):
        t = list(t)
        i = 0
        while i < len(t):
            t[i], check = convertSingle(t[i])
            i += 1
        t = tuple(t)
    return t

def testProgram():
    c = ("12398", "1978", "278")
    print(c)
    c = convert(c)
    print(c)
    """
    for e in c:
        print(e, type(e))
    """

    print("")

    c = {"True" : "123", "123" : "test"}
    print(c)
    c = convert(c)
    print(c)

    print("")

    c = {"True" : "123", "123" : "test", 123 : "test2"}
    print(c)
    """
    for k, v in c.items():
        print(k, type(k), v, type(v))
    """
    c = convert(c)
    print(c)
    """
    for k, v in c.items():
        print(k, type(k), v, type(v))
    """

    print("")
    for index, element in ["a", "b", "c"]:
        print(index, " ", element)

testProgram()