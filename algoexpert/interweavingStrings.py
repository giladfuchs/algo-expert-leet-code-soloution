def interweavingStrings(one, two, three):
    res = ''
    for ch in three:
        take_some = False
        if one[0] == two[0]:
            if interweavingStrings(two, one, three[len(res) + 1:]):
                return True
        if one and one[0] == ch:
            take_some = True
            res += one[0]
            one = one[1:]
        elif two and two[0] == ch:
            take_some = True
            res += two[0]
            two = two[1:]
        if not take_some:
            if ch in one:
                index_one = one.index(ch)
                one = one[index_one + 1:]
            elif ch in two:
                index_one = two.index(ch)
                two = two[index_one + 1:]
            else:
                return False

    return res == three


print(interweavingStrings("algoexpert", "your-dream-job", "your-algodream-expertjob"))
