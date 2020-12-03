#%%
from collections import Counter
with open('input2.txt', 'r') as f:
    x = f.readlines()


#%%
part_one = False
part_two = True

N_ok = 0
for el in x:
    n_min = int(el.split('-')[0])
    n_max = int(el.split('-')[1].split()[0])
    letter = el.split(':')[0][-1]
    passw = el.split(':')[1].strip()
    cntr = Counter(passw)
    if part_one: 
        if letter not in cntr:
            print(f'No {letter} in {passw}')
            continue
        if n_min <= cntr[letter] <= n_max:
            N_ok += 1
            print(f'+1: {cntr[letter]:2} {letter} in {v}. In range {n_min}-{n_max}')
            continue
        print(f'--: {cntr[letter]:2} {letter} in {v}. Not in range {n_min}-{n_max}')
    if part_two:
        if (passw[n_min-1]==letter) != (passw[n_max-1]==letter):
            N_ok +=1


print(N_ok)




# %%
