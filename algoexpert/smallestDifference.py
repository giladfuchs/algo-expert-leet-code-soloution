def smallestDifference(arrayOne, arrayTwo):



    def check_abs(arr_tow):
        return abs(arr_tow[0]-arr_tow[1])

    ans = [arrayOne[0], arrayTwo[0]]
    n = len(arrayOne)
    m = len(arrayTwo)

    arrayOne.sort()
    arrayTwo.sort()
    index = 0
    j = 0
    while j<m:
        while index<n and arrayOne[index]< arrayTwo[j]:
            index+=1

        if index<n and check_abs([arrayOne[index], arrayTwo[j]]) < check_abs(ans):
            ans[0] = arrayOne[index]
            ans[1] = arrayTwo[j]

        if index>0 and check_abs([arrayOne[index-1], arrayTwo[j]]) < check_abs(ans):
            ans[0] = arrayOne[index-1]
            ans[1] = arrayTwo[j]
        if index==n:
            index-=1
        j+=1


    return ans

print(smallestDifference([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17]))