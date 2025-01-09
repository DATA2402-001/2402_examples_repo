
def compound_interest(pv: float, r: float, t:float) -> float:
    """
    compute future value given PV, r, t
    :param pv: present value
    :param r: interest rate in %
    :param t: time in years
    """
    fv = pv * (1 + r/100) ** t
    return fv

print(compound_interest(100, 15, 10))