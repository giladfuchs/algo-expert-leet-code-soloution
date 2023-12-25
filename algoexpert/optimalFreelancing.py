def optimalFreelancing(jobs):
    jobs.sort(key=lambda job: job.get('payment'), reverse=True)
    res = []
    deadLines = []

    for job in jobs:
        if len(res) == 7:
            break
        deadline = job.get('deadline')
        if deadline > len(res) or deadline not in deadLines:
            res.append(job.get('payment'))
            deadLines.append(deadline)

    return sum(res)


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
