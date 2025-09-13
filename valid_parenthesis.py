def valid_parenthesis(s):
    mapping = {')':'(' ,'}':'{',']':'['}
    st = []
    for i in s:
        if i in mapping:
            top = st.pop() if st else None
            if mapping[i] != top:
                return False
        else:
            st.append(i)
    return not st
print(valid_parenthesis("({[]})"))