def is_anagram(str1,str2):
    hash1 = {}
    hash2 = {}
    for char in str1:
        hash1[char] = hash1.get(char, 0) + 1
    for char in str2:
        hash2[char] = hash2.get(char, 0) + 1
    if hash1 == hash2:
        return True
    return False

str1 = "silent"
str2 = "silent"
print(is_anagram(str1,str2))
