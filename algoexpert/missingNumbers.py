def missingNumbers(nums):
    ans = []
    n = len(nums)
    nums += [n + 3, n + 3]
    for i in range(n):
        num = abs(nums[i]) - 1
        nums[num] *= -1
    for i in range(n + 2):

        if nums[i] > 0:
            ans.append(i + 1)
    return ans


if __name__ == '__main__':
    print(missingNumbers([1, 4, 3]))
