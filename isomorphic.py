def isomorphic(a1,a2):
    if len(a1) != len(a2):
        return False
    map1 = {}
    map2 = {}
    for i in range(len(a1)):
        if a1[i] in map1:
            if map1[a1[i]] != a2[i]:
                return False
            else:
                map1[a1[i]] = a2[i]

            if a2[i] in map2:
                if map2[a2[i]] != a1[i]:
                    return False
                else:
                    map2[a2[i]] = a1[i]

    return True
print(isomorphic("bat", "cat"))