def two_sum_ii(numbers:[int], target:int)->[int]:
    d = {numbers[i] :i for i in range(len(numbers))}
    for i in range(len(numbers)):
        if (target - numbers[i] )in d.keys():
            return [i+1, d[target - numbers[i]]+1]

    return 0

# print(two_sum_ii(numbers=[2,7,11,15],target= 9))
def func(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1

print(func(numbers=[1,4,5,6,7,11,13,14,17],target= 21))
