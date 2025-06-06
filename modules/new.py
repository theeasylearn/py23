# 1) import filename
# 2) from filename import fun

import maths as m

m.add(2,4)
m.sub(3,6)
m.div(3,6)
m.mul(3,6)

# from maths import add,div
# add(3,4)

# div(2,3)

from maths import *

add(1,2)
sub(3,4)
div(4,5)

import maths
# print(dir(maths))
for i in dir(maths):
    print(i)
    