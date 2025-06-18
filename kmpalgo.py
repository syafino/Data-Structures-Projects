def KMPmatch(pattern, text):
    Prefix = [-1] * len(pattern)

    def prefix(i):
        if Prefix[i] == -1:
            if i == 1:
                Prefix[i] = 0
            else:
                Prefix[i] = extend(prefix(i - 1), pattern[i - 1])
        return Prefix[i]

    def extend(j, c):
        if j < len(pattern) and pattern[j] == c:
            return j + 1
        if j == 0:
            return 0
        return extend(prefix(j), c)

    def match(m, n):
        if m == len(pattern):
            return n - m
        if n == len(text):
            return -1
        return match(extend(m, text[n]), n + 1)

    return match(0, 0)

