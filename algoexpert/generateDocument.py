from collections import Counter


def generateDocument(characters, document):
    char_counter = Counter(characters)
    doc_count = Counter(document)
    for c, count in doc_count.items():
        if char_counter.get(c, 0) < count:
            return False
    return True
