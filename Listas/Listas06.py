def is_anagram(first, second):
    return sorted(first) == sorted(second)

print(is_anagram('a','a'))