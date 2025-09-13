from collections import Counter
def couting_char(s):
    dict = Counter(s)
    for c in s:
        if dict[c] == 1:
            return c
    return None

print(couting_char("Hello World"))

