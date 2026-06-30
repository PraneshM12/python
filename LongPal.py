def long_pal(s):
    long =""
    for i in range(len(s)):
        for j in range(i,len(s)):
            sub = s[i:j+1]
            if sub == sub[::-1] and len(sub)> len(long):
                long= sub
    return long

print(long_pal("abbacbabcaaabacacaba"))

