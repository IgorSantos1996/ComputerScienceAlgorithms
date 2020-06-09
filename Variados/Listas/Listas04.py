def chop(listinha):
    del listinha[0]
    del listinha[-1]
    return listinha

print(chop([1, 2, 3, 4]))