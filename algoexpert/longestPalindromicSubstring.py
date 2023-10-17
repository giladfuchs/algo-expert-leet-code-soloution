def longestPalindromicSubstring(string):
    maxi = string[0]
    for i in range(len(string)):
        temp = string[i]
        for j in range(i + 1, len(string)):
            temp += string[j]
            if temp == temp[::-1] and len(temp)> len(maxi):
                maxi=temp
    return maxi

if __name__ == '__main__':
    print(longestPalindromicSubstring("abaxyzzyxf"))
