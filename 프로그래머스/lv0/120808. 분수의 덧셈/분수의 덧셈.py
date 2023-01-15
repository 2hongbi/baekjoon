import math

    
def solution(numer1, denom1, numer2, denom2):
    top = denom1 * denom2
    bottom = numer1 * denom2 + numer2 * denom1
    
    gcd = math.gcd(top, bottom)
    
    return [bottom / gcd, top / gcd]