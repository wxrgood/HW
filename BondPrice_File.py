

def getBondPrice(y, face, couponRate, m, ppy=1):
    pvcfsum = 0
    cf = couponRate * face
    for t in range(1, m+1):
        pv = (1+y)**(-t)
        pvcf = pv * cf
        pvcfsum += pvcf
    bondprice = pvcfsum + pv * face
    return(bondprice)