class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        arr[0] = 1  # first condition

        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) <= 1:
                continue  # purposely wrote for understanding
            else:
                arr[i] = arr[i - 1] + 1  # second condition

        return arr[-1]

print(Solution().maximumElementAfterDecrementingAndRearranging([2,2,1,2,1]))