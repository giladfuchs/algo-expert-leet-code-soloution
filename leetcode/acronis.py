# exist_sample = set(['1sfdfsd','2',])
# sample2 = ['1','2',]
# exist_sample = set(list(exist_sample) + sample2)
# for sm in sample2:
#
#     if not sm in exist_sample:
#         exist_sample.add(sm)
#
#
#aa aaa bbb
#aa aaa bbb
#aa aaa bbb
content = open('file.txt','r').read().split('\n')
res = [ len(line.split(' ')) for line in content]
print(res)
try:
    content = open('file.txt','r')
    res  = [ len(line.split(' ')) for line in content]
    content.close()
except Exception as e:
    try:
        if content:
            content.close()
    except:
        pass
    print(f'error: {e}')





