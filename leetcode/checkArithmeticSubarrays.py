class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        result = []
        for i in range(len(l)):
            result.append(self.is_arithmetic(nums, l[i], r[i]))
        return result

    def is_arithmetic(self, nums, l, r):
        max_val, min_val = max(nums[l:r + 1]), min(nums[l:r + 1])


        length = r - l + 1
        if (max_val - min_val) % (length - 1) != 0:
            return False

        diff = (max_val - min_val) // (length - 1)
        if diff == 0:
            return True

        visited = [False] * length

        for i in range(l, r + 1):
            val = nums[i]
            if (val - min_val) % diff != 0:
                return False
            else:
                pos = (val - min_val) // diff
                if visited[pos]:
                    return False
                visited[pos] = True
        return True


print(Solution().checkArithmeticSubarrays([-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], l=[0, 1, 6, 4, 8, 7],
                                          r=[4, 4, 9, 7, 9, 10]))
