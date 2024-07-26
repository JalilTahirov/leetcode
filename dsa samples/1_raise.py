def raisenumber(number, exp):
    if exp == 0:
        return 1
    else:
        return number * raisenumber(number, exp-1)
    
v = raisenumber(2,2)
print(v)
    