def compound_interest_amount(p,r,t,n):
    return p * ( 1 + r / n) ** (n*t)

print(compound_interest_amount(10000,0.1,4,4))