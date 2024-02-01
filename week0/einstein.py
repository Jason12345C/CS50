def main():
    #prompt user to enter mass
    m = int(input("m: "))
    #use mass-energy equivalence equation and print
    #the function einstein accepts mass as argument and returns energy as output
    e = einstein(m)
    print(f"{e:,}")

#define einstein as mass energy equation, define c
#return energy
def einstein(m):
    c = 300000000
    e = m*(c**2)
    return e

main()