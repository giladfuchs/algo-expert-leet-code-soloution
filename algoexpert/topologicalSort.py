from collections import defaultdict


def topologicalSort(jobs, deps):
    d_sec_job = defaultdict(list)
    firsts = set()
    for x, y in deps:
        d_sec_job[y].append(x)
        firsts.add(x)
    res = []
    sec_job = list(d_sec_job.keys())
    for job in jobs:
        if job in firsts and job not in sec_job:
            res.append(job)

    while d_sec_job:
        sec_job = list(d_sec_job.keys())
        for sec in sec_job:
            if not [key for key in d_sec_job[sec] if key not in res]:
                res.append(sec)
                d_sec_job.pop(sec)
    return res
print(topologicalSort([1, 2, 3, 4, 5, 6, 7, 8],[
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 8],
    [8, 1]
]))