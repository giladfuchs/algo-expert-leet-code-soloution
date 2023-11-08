from collections import Counter
def minimumCharactersForWords(words):
    main_counter = {}
    for word in words:
        temp_count = Counter(list(word))
        for char, count in temp_count.items():
            main_counter[char] = max(count, main_counter[char]) if char in main_counter else count

    res = []
    for char, count in main_counter.items():
        for _ in range(count):
            res.append(char)
    return res


print(minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]))
