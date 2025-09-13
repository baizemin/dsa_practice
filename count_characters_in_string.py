def count_chars(s):
    v = 0
    con = 0
    sp = 0
    digits = 0
    vowels = 'aeiou'
    for c in s:
        c = c.lower()
        if c == ' ':
            sp+=1
        if c.isdigit():
            digits+=1
        if c in vowels:
            v+=1
        elif 'a' < c <= 'z':
            con+=1
    return sp, v, con, digits
input_string = "Hello World 123"
print(count_chars(input_string))

