from collections import defaultdict


def tournamentWinner(competitions, results):
    # Write your code here.
    counter = defaultdict(int)
    for i, _ in enumerate(competitions):
        counter[_[::-1][results[i]]] += 3

    winner = max(counter, key=counter.get)
    return winner


if __name__ == '__main__':
    print(tournamentWinner([
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ], [0, 0, 1]))
