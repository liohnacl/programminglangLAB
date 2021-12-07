def valInput():
    try:
        container = list(map(int,input("Enter number/s with the use of * (asterisk) for getting its product: ").split('*')))
        return container
    except Exception:
        print("INVALID INPUT...")

def mutiplyingVals(values):
    try:
        prod = 1
        for a in values:
            prod *=a
        return prod
    except Exception:
        print("INVALID INPUT.....")

if __name__ == "__main__":
    col = valInput()
    product = mutiplyingVals(col)
    print(f"The product of the inputted numbers is: {product}")