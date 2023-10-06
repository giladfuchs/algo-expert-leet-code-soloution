import re

mat = [['T', 's', 'i'], ['h', '%', 'x'], ['i', ' ', '#'], ['s', 'M', ' '], ['$', 'a', ' '], ['#', 't', '%'],
       ['i', 'r','!']]
a = list(zip(*mat))
b = ''
for z in zip(*mat):
    b += "".join(z)
print(a)
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))

# a = '''7 3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ir!'''
# mat = []
# temp = []
# for _ in a:
#
#     if _ != '\n':
#         temp.append(_)
#     else:
#         mat.append(temp[:])
#         temp = []
#
# print(mat)
