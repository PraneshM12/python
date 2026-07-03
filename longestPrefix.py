def long_suf(q1,q2):
    result = ""
    i = len(q1)-1
    j = len(q2)-1
    while i >= 0 and j >= 0:
        if q1[i] != q2[j]:
            break
        result = q1[i] + result
        i -=1
        j -=1
    return result
print(long_suf("bating", "bowling"))
