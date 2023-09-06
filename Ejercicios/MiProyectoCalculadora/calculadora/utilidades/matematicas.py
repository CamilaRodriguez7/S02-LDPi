def mcm(a, b):
    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // gcd(a, b)

def mcd(a, b):
    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    if a == 0 or b == 0:
        return max(a, b)
    else:
        return gcd(a, b)