
def getBondDuration(y, face, couponRate, m, ppy=1):
    coupon_payment = face * couponRate / ppy
    period_yield = y / ppy
    total_periods = m * ppy
    coupon_PVs = sum(coupon_payment / ((1 + period_yield)**t) for t in range(1, total_periods + 1))
    face_value_PV = face / ((1 + period_yield)**total_periods)
    bond_price = coupon_PVs + face_value_PV
    weighted_times = sum(t * (coupon_payment / ((1 + period_yield)**t)) for t in range(1, total_periods + 1))
    final_term = total_periods * (face / ((1 + period_yield)**total_periods))
    bondDuration = (weighted_times + final_term) / bond_price
    return bondDuration