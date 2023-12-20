def optimalFreelancing(jobs):
    jobs.sort(key=lambda job: job.get('payment'), reverse=True)
    day, i = 1, 0
    res = 0
    for job in jobs:
        if day == 7:
            return res
        if day < job.get('deadline'):
            res += job.get('payment')
            day += 1    

    # while i < len(jobs):
    #     day += 1
    #     temp = 0
    #     while i < len(jobs) and day == jobs[i].get('deadline'):
    #         temp = max(temp, jobs[i].get('payment'))
    #         i += 1
    #     res += temp
    return res


print(optimalFreelancing([

    {
        "deadline": 2,
        "payment": 1
    },
    {
        "deadline": 1,
        "payment": 4
    },
    {
        "deadline": 3,
        "payment": 2
    },
    {
        "deadline": 1,
        "payment": 3
    },
    {
        "deadline": 4,
        "payment": 3
    },
    {
        "deadline": 4,
        "payment": 2
    },
    {
        "deadline": 4,
        "payment": 1
    },
    {
        "deadline": 5,
        "payment": 4
    },
    {
        "deadline": 8,
        "payment": 1
    }
]))
