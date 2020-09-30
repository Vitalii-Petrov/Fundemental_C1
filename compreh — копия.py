# exa 1
words = "Hello big world!".split()
print([len(word) for word in words])
#print(list)

# exa 2
import os
import glob
from pprint import pprint as pp

print('2)')
for p in glob.glob('*.py'):
    pp(os.path.realpath(p))

print('3)')
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
pp(file_sizes)