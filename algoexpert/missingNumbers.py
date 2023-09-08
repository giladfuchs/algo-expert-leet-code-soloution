def missingNumbers(nums):
    ans = []
    for i in range(1, len(nums) + 3):
        if i not in nums:
            ans.append(i)
    return ans


if __name__ == '__main__':
    print(missingNumbers([1,4,3]))