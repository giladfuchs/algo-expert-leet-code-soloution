def shortenPath(path):
    ans = '/' if path[0] == '/' else ''
    split_path = path.split('/')
    temp = []
    for way in split_path:
        if not way or way == '.':
            continue
        if (not ans and (not temp or temp[-1] == '..')) or way != '..':
            temp.append(way)
        elif temp:
            temp.pop()
    return ans + '/'.join(temp)


if __name__ == '__main__':
    print(shortenPath("/../../foo/bar/baz"))
    print(shortenPath("../../foo/bar/baz"))
