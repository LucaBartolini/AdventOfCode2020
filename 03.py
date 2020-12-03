'''
https://adventofcode.com/2020/day/3
'''

#%%
with open(r'inputs\input3.txt', 'r') as f:
    x = f.readlines()

x = [el.strip() for el in x]
width = len(x[0])

#%%
right_step = [1,3,5,7,1]
down_step = [1,1,1,1,2]

def count_trees(x, right_step, down_step):
    N_trees = 0
    for i,row in enumerate(x[::down_step]):
        if row[(i*right_step) % width] == '#':
            N_trees += 1
    return N_trees

# %%
import math
res = [count_trees(x,r,d) for r,d in zip(right_step, down_step)]
print(math.prod(res))
    
# %%

# %%
