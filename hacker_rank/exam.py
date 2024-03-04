import requests


def getCapitalCity(country):
    res = requests.get(f'https://jsonmock.hackerrank.com/api/countries?name={country}')
    data = res.json().get('data')
    if not data:
        return '-1'
    capital = data[0].get('capital', '-1')
    return capital


from collections import defaultdict


def getSum(n):
    ans = 0
    while n != 0:
        ans = ans + (n % 10)
        n = n // 10

    return ans



# '''
# SELECT c.NAME, o.PRICE
# FROM customers c INNER JOIN orders o
# ON c.ORDER_ID = o.ID
# WHERE o.ORDER_DATE <= (SELECT MIN(ORDER_DATE) FROM orders) + INTERVAL 10 YEAR
#   AND o.PRICE = (SELECT MAX(PRICE) FROM orders WHERE ORDER_DATE <= (SELECT MIN(ORDER_DATE) FROM orders) + INTERVAL 10 YEAR);
# '''
def findMaxNum(x, y, z):
    step = abs(x - y)
    z -= step
    if z < 0:
        return -1
    if z == 0:
        return max(x, y)
    res = z // 2 + max(x, y)
    return res


def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


def waysToChooseSum(lowLimit, highLimit):
    counter_win = defaultdict(int)
    for i in range(lowLimit, highLimit + 1):
        counter_win[sum_digits(i)] += 1
    print(sum_digits(i), i)
    print(counter_win)
    values = list(counter_win.values())
    max_value = max(values)
    winners = [_ for _ in values if _ == max_value]
    ways = len(winners)
    winners = max_value
    return [ways, winners]

from collections import defaultdict


def solution(arr):
    d = defaultdict(list)
    d[arr[0] + arr[1]].append(0)
    for i in range(1, len(arr) - 1):
        temp1 = arr[i] + arr[i + 1]
        if i - 1 not in d[temp1]:
            d[temp1].append(i)

    return len(max(d.values(), key=len))



if __name__ == '__main__':
    # print(getCapitalCity('spain'))
    # print(findMaxNum(4, 4, 4))
    print(waysToChooseSum(3, 1144))
    # print(waysToChooseSum(1, 5))
    # print(findMaxNum(44, 48, 6))
    # print(findMaxNum(8,5,3))

    print(solution([10, 1, 3, 1, 2, 2, 1, 0, 4]))
    print(solution([9, 9, 9, 9, 9]))
    print(solution([1, 5, 2, 4, 3, 3]))