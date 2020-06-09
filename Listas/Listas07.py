def has_duplicates(listinha):
    t = list(listinha)
    t.sort()
    for z in range(len(t)-1):
        if t[z] == t[z+1]:
            return True
    return False

print(has_duplicates(['a','u','t','y']))