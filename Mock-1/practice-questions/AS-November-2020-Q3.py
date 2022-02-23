X = int(input("Enter an integer greater than 1: "))
Product = 1
Factor = 0
while Product < X:
    Factor += 1
    Product = Product * Factor

if X == Product:
    Product = 1
    for N in range(1, Factor+1):
        Product = Product * N
        print(N)
else:
    print("No Result")