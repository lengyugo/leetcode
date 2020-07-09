import collections
def maxAliveYear( birth, death) -> int:
    b = collections.Counter(birth)
    #print(b)
    d = collections.Counter(death)
    #print(d)
    ans, maxcount, cur = 0, 0, 0
    #print(sorted({*b.keys(), *d.keys()}))
    for year in sorted({*b.keys(), *d.keys()}):

        cur += b[year]
        if cur > maxcount:
            maxcount = cur
            ans = year
        cur -= d[year]
    return ans

a = maxAliveYear([1972,1908,1915,1957,1960,1948,1912,1903,1949,1977,1900,1957,1934,1929,1913,1902,1903,1901],
[1997,1932,1963,1997,1983,2000,1926,1962,1955,1997,1998,1989,1992,1975,1940,1903,1983,1969])
print(a)
