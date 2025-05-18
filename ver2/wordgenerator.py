import itertools

chrs = 'abcdefghijklmnopqrstuvwxyz'
n = 5
for xs in itertools.product(chrs, repeat=n):
    print(''.join(xs))