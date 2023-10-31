def build_suffix_array(s):
    n = len(s)
    rank = [ord(ch) for ch in s]
    sa = list(range(n))
    temp = [0] * n
    def get_rank(i):
        return rank[i] if i < n else -1

    t = 1
    while t <= n:
        sa.sort(key=lambda x: (get_rank(x), get_rank(x + t)))
        p = 0
        temp[sa[0]] = 0
        for i in range(1, n):
            if get_rank(sa[i - 1]) != get_rank(sa[i]) or get_rank(sa[i - 1] + t) != get_rank(sa[i] + t):
                p += 1
            temp[sa[i]] = p
        rank = temp[:]
        t <<= 1

    return sa, rank


def build_lcp(word, sa, rank):
    word_len = len(word)
    lcp = [0] * word_len
    length = 0

    for i in range(len(word)):
        if rank[i] == 0:
            continue
        j = sa[rank[i] - 1]
        while i + length < word_len and j + length < word_len and word[i + length] == word[j + length]:
            length += 1
        lcp[rank[i]] = length
        length = max(length - 1, 0)

    return lcp


if __name__ == "__main__":
    words = [input(), input()]
    word = "#".join(words)
    sa, rank = build_suffix_array(word)
    lcp = build_lcp(word, sa, rank)

    m = (0, 0)
    for i, length in enumerate(lcp):
        if 0 <= sa[i - 1] + length - 1 < len(words[0]) and len(words[0]) < sa[i] + length - 1 < len(word):
            m = max(m, (length, i))

        if 0 <= sa[i] + length - 1 < len(words[0]) and len(words[0]) < sa[i - 1] + length - 1 < len(word):
            m = max(m, (length, i))

    length, start = m
    print(length)
    print(word[sa[start]:sa[start] + length])