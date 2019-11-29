import gmpy2 as gmp

private_key = open("./private_key.txt", "r+")
private = str.splitlines(private_key.read())
private_key.close()
d = gmp.mpz(private[0][2:])
n = gmp.mpz(private[1][2:])
public_key = open("./public_key.txt", "r+")
public = str.splitlines(public_key.read())
public_key.close()
e = gmp.mpz(public[0][2:])

# UI
while True:
    mode = input("Please choose 1 for encrypt and 0 for decrypt:")
    if mode == "1":
        plain = gmp.mpz(input("Please input plaintext:"))
        # powmod(x, y, m) returns (x ** y) mod m
        cipher = gmp.powmod(plain, e, n)
        print("plaintext={0}\nThe encrypted result is {1}".format(plain, cipher))
    else:
        cipher = gmp.mpz(input("Please input ciphertext:"))
        plain = gmp.powmod(cipher, d, n)
        print("ciphertext={0}\nThe decrypted result is {1}".format(cipher, plain))


