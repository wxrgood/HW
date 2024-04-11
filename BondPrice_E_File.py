

def getBondPrice_E(face, couponRate, m, yc):
    bondPrice = 0t
    coupon_payment = face * couponRate
    for t, y in enumerate(yc, start=1):
        bondPrice += coupon_payment / ((1 + y)**t)
        if t == m:
            bondPrice += face / ((1 + y)**t)
            
    return bondPrice

