from random import randint

# Reference: https://stackoverflow.com/questions/42324419/karatsuba-multiplication-implementation

def karat(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = m // 2

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)

        z0 = karat(b,d)
        z1 = karat((a+b),(c+d))
        z2 = karat(a,c)

        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)

def randomdigits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def mul(x,y):
	return (x*y)

for x in range(1,1001):
	number_one = randomdigits(512)
	number_two = randomdigits(512)
	# print("#",x," \t", number_one,'x', number_two,' = ', karat(number_one,number_two))
	print("#",x," \t", number_one,'x', number_two,' = ', mul(number_one,number_two))

print("For n = 512")
