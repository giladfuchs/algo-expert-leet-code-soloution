def caesarCipherEncryptor(string, key):
    ans = ''
    for ch in string:
        char = ord(ch) + key - 97
        char %= 26
        ans += chr(char + 97)

    return ans


print(caesarCipherEncryptor("xyz", 2))
