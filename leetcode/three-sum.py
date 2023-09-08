
def threeSum(nums:[int]):
    nums.sort()
    length = len(nums)
    ans = []
    for i in range(length):
        if i and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = length - 1
        while j < k:
            if k < length - 1 and nums[k] == nums[k+1]:
                k -= 1
                continue
            temp = nums[i] + nums[j] + nums[k]
            if temp < 0:
                j += 1
            elif temp > 0:
                k -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

    print(ans)
threeSum([-1,0,1,2,-1,-4,2,2,2,5,5,5])