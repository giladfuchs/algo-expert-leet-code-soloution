space = ' '


def reverseWordsInString(string):
    ans = []
    last = ''
    temp = ''
    for char in string:
        # if char==space:
        if last == space  :
            ans.insert(0, temp)
            temp = char
        else:
            temp += char
        last = char
    ans.insert(0, temp + space)

    # Write your code here.
    return ''.join(ans)[:-1]


if __name__ == '__main__':
    print(reverseWordsInString("test        "))
