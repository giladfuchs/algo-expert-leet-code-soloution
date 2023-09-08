def solution1(numbers):
    ans = []
    for i in range(len(numbers)-2):
        if (numbers[i] < numbers[i+1] and numbers[i+1] > numbers[i+2]) or \
                (numbers[i] > numbers[i + 1] and numbers[i + 1] < numbers[i + 2]) :
            ans.append(1)
        else:
            ans.append(0)
    return ans
def solution2(a):
    b = []
    i=0
    n = len(a)-1
    while i<n:
        b.append(a[i])
        b.append(a[n])
        i+=1
        n-=1
        if i==n:
            b.append(a[i])

    for _ in range(len(b)-1):
        if b[_+1] <= b[_]:
            return False
    return True

# print(solution2([-91, -84, -67, -44, 9, 70, 88, 37, -11, -67, -72, -87]))

CURSOR = '|'
MAX_LEN=20
def out_cursor(word):

    index = next((i for i, c in enumerate(word) if c==CURSOR),-1 )
    if index>=0:
        word = ''.join([word[:index],word[index+1:]])
    return word , index
def insert_cursor(word, index):
    word = f"{word[:index]}{CURSOR}{word[index:]}"

    return word
def solution(operations):
    text = ''
    for ope in operations:
        comand, other = ope.split(' ')
        if comand == "TYPE":
            if len(other)> MAX_LEN:
                other = other[:MAX_LEN]
            text, index = out_cursor(text)
            if index>-1:
                text = f"{text[:index]}{other}{CURSOR}{text[index:]}"
            else:
                text = f"{text}{other}{CURSOR}"

        # if comand == "SELECT":
        #
        if comand == "MOVE_CURSOR":
            text, index = out_cursor(text)
            insert_cursor(text, int(other))
        # if comand == "UNDO":
    return text
print(solution( ["TYPE Code", "TYPE Signal"]))