#%%
with open('input1.txt', 'r') as f:
    x = f.readlines()

x = [int(el) for el in x]

#%%

for i, el1 in enumerate(x[:-1]):
    for j,el2 in enumerate(x[i+1:]): 
        for el3 in x[j+1:]:
            if el1+el2+el3 == 2020:
                print(el1)
                print(el2)
                print(el3)
                print(el1*el2*el3)
                break
# %%
