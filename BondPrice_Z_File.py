

def getBondPrice_Z(face, couponRate, times, yc):
    bondPrice = 0
    coupon_payment = face * couponRate
    for time, yield_rate in zip(times, yc):
        bondPrice += coupon_payment / ((1 + yield_rate)**time)
    bondPrice += face / ((1 + yc[-1])**times[-1])

    return bondPrice
