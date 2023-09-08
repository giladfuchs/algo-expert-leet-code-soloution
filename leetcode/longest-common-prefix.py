def longest_common_prefix(str_list: [str]) -> str:

    prefix = str_list[0] if str_list else ""
    
    for s in str_list:
        while prefix not in s and prefix:
            prefix = prefix[:len(prefix) - 1]

        if not prefix:
            return prefix

    return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog","racecar","car"]))
