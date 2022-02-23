def largest(min_factor, max_factor):
    pals = pproducts(min_factor, max_factor)
    if len(pals) == 0:
        return (None, [])
    else:
        return (pals[-1][0], [f for (s, f) in pals if s == pals[-1][0]])
def smallest(min_factor, max_factor):
    pals = pproducts(min_factor, max_factor)
    if len(pals) == 0:
        return (None, [])
    else:
        return (pals[0][0], [f for (s, f) in pals if s == pals[0][0]])
def pproducts(min, max):
    if max < min:
        raise ValueError("Max is lower than min")
    prods = [(i*j, [i,j]) for i in range(min, max+1) for j in range(i,max+1) if str(i*j)[::-1] == str(i*j)]
    return sorted(prods, key=lambda x:x[0])
