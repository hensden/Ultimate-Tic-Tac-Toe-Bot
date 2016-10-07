"""Generate req list."""

k = 0
for i in xrange(81):
    print "{}, {}, {},".format(k, k + 1, k + 2),
    k += 3
    if k == 9:
        k = 0
a = [0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 3, 4, 5, 3, 4, 5, 6, 7, 8, 6, 7, 8,
     6, 7, 8, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 3, 4, 5, 3, 4, 5, 6, 7, 8,
     6, 7, 8, 6, 7, 8, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 3, 4, 5, 3, 4, 5,
     6, 7, 8, 6, 7, 8, 6, 7, 8]
print "\n"
b = []
for i in a:
    if i == 0:
        b.append([1, 3])
    elif i == 1:
        b.append([0, 2])
    elif i == 2:
        b.append([1, 5])
    elif i == 3:
        b.append([0, 6])
    elif i == 4:
        b.append([4])
    elif i == 5:
        b.append([2, 8])
    elif i == 6:
        b.append([3, 7])
    elif i == 7:
        b.append([6, 8])
    elif i == 8:
        b.append([5, 7])

print b
