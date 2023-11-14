def semordnilap(words):
    words_set = set()
    ans = []
    for w in words:
        if w[::-1] in words_set:
            ans.append([w, w[::-1]])
        else:
            words_set.add(w)
    return ans


print(semordnilap(["diaper", "abc", "test", "cba", "repaid"]))
