import gmpy2 as gmp
import random

# 1.generate p,q
# 2.n=p*q, phin=(p-1)(q-1)
# 3.e=65537
# 4.d ed=1 mod phin
# 5.c=p^e mod n
# 6.p=c^d mod n

def init_prime():
    flag = False
    while not flag:
        seed = random.randint(0, 1024)
        state = gmp.random_state(seed)
        init = gmp.mpz_urandomb(state, 128)
        prime = gmp.next_prime(init)
        flag = gmp.bit_length(prime) == 128
    return prime


p = init_prime()
q = init_prime()

n = gmp.mul(p, q)
phin = gmp.mul(gmp.add(p, -1), gmp.add(q, -1))

e = gmp.mpz(65537)
# e*d =1 mod phin
d = gmp.invert(e, phin)

private_key = open("./private_key.txt", "w+")
print("d={0}\nn={1}".format(d, n), file=private_key)
private_key.close()

public_key = open("./public_key.txt", "w+")
print("e={0}\nn={1}".format(e, n), file=public_key)
public_key.close()

print("p={0}".format(p))
# print("p is prime = {0}; p_length = {1}".format(gmp.is_prime(p), gmp.bit_length(p)))
print("q={0}".format(q))
# print("q is prime = {0}; q_length = {1}".format(gmp.is_prime(q), gmp.bit_length(q)))
print("e={0}".format(e))
print("d={0}".format(d))
print("n={0}".format(n))
print("Phi(n)={0}".format(phin))

