from collections import defaultdict


def stableInternships(interns, teams):
    # Write your code here.
    already_set = set()
    ans = []
    for i, prefer in enumerate(teams):
        student_prefer = defaultdict(int)
        for j, team_index in enumerate(prefer):
            student_prefer[team_index] += (3 - j)

            index_prefer = interns[team_index].index(i)
            student_prefer[team_index] += (3 - index_prefer)
        print(student_prefer)

        # ans.append(student_prefer)

        while student_prefer:
            winner = max(student_prefer, key=student_prefer.get)
            student_prefer.pop(winner)
            if winner not in already_set:
                already_set.add(winner)
                ans.append([winner, i])
                break
    return ans


if __name__ == '__main__':
    print(stableInternships(**{
        "interns": [
            [0, 1, 2],
            [0, 1, 2],
            [0, 1, 2]
        ],
        "teams": [
            [2, 1, 0],
            [2, 1, 0],
            [2, 1, 0]
        ]
    }))
