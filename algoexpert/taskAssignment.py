def taskAssignment(k, tasks):
    sort_tasks = sorted(tasks)
    ans = []
    st = 0
    end = len(tasks)-1
    def get_index(num):
        index = next((i for i, _ in enumerate(tasks) if _ == num))
        tasks[index] = 0
        return index
    while st < end:
        index1, index2 = get_index(sort_tasks[st]), get_index(sort_tasks[end])
        ans.append([index1, index2])
        end-=1
        st+=1
    return ans
print(taskAssignment(3, [1, 3, 5, 3, 1, 4]))